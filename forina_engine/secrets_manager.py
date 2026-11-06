"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
LOCAL SECRETS VAULT & WORKSPACE CREDENTIAL MANAGER
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
import base64
import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Dict, Any, Optional

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class SecretsManager:
    """Manages workspace API secrets (Mistral, GitHub, Providers) locally with AES-GCM encryption."""

    def __init__(self, project_root: Path | str):
        self.root = Path(os.path.abspath(project_root))
        self.vault_file = self.root / "config" / ".secrets_vault.bin"
        self.salt_file = self.root / "config" / ".vault_salt.bin"
        self._key = self._derive_master_key()

    def _derive_master_key(self) -> bytes:
        self.salt_file.parent.mkdir(parents=True, exist_ok=True)
        if self.salt_file.exists():
            salt = self.salt_file.read_bytes()
        else:
            salt = os.urandom(16)
            self.salt_file.write_bytes(salt)
            try:
                os.chmod(self.salt_file, stat.S_IRUSR | stat.S_IWUSR)
            except Exception:
                pass

        # Use machine/project identifier seed for deterministic local unlocking
        seed = f"{self.root}:{os.environ.get('USER', 'hcos')}".encode("utf-8")
        return hashlib.pbkdf2_hmac("sha256", seed, salt, 100_000, dklen=32)

    def load_secrets(self) -> Dict[str, str]:
        if not self.vault_file.exists():
            return {}
        try:
            data = self.vault_file.read_bytes()
            if len(data) < 12:
                return {}
            nonce, ciphertext = data[:12], data[12:]
            aesgcm = AESGCM(self._key)
            decrypted = aesgcm.decrypt(nonce, ciphertext, None)
            return json.loads(decrypted.decode("utf-8"))
        except Exception:
            return {}

    def set_secret(self, key: str, value: str) -> bool:
        secrets = self.load_secrets()
        secrets[key] = value
        try:
            plaintext = json.dumps(secrets).encode("utf-8")
            nonce = os.urandom(12)
            aesgcm = AESGCM(self._key)
            ciphertext = aesgcm.encrypt(nonce, plaintext, None)
            self.vault_file.write_bytes(nonce + ciphertext)
            try:
                os.chmod(self.vault_file, stat.S_IRUSR | stat.S_IWUSR)
            except Exception:
                pass
            return True
        except Exception:
            return False

    def get_secret(self, key: str, default: Optional[str] = None) -> Optional[str]:
        # Check env var first, then vault
        if key in os.environ:
            return os.environ[key]
        return self.load_secrets().get(key, default)

    def get_vault_summary(self) -> Dict[str, Any]:
        secrets = self.load_secrets()
        return {
            "vault_active": True,
            "keys_configured": list(secrets.keys()),
            "total_secrets": len(secrets),
            "storage": "Local Encrypted AES-256-GCM (Zero Cloud Leak)",
            "isolated": True
        }
