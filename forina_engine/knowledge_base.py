"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
KNOWLEDGE BASE, VECTOR SEARCH & WEBSITE INDEXER
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
import hashlib
import json
import math
import os
import re
import time
from pathlib import Path
from typing import Dict, Any, List, Optional


def _pseudo_embedding(text: str, dim: int = 256) -> List[float]:
    """
    Deterministic local semantic vector representation (128, 256, 1024 dims).
    Runs offline without requiring external API or heavy GPU dependencies.
    """
    tokens = re.findall(r"\w+", text.lower())
    vec = [0.0] * dim
    for i, tok in enumerate(tokens):
        h = int(hashlib.md5(tok.encode("utf-8")).hexdigest(), 16)
        slot = h % dim
        val = ((h >> 8) % 1000) / 1000.0 - 0.5
        vec[slot] += val / (1.0 + math.log(1 + i))

    # Normalize vector to unit length
    norm = math.sqrt(sum(x * x for x in vec)) or 1.0
    return [round(x / norm, 5) for x in vec]


def _cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    dim = min(len(vec_a), len(vec_b))
    dot = sum(vec_a[i] * vec_b[i] for i in range(dim))
    return max(0.0, min(1.0, (dot + 1.0) / 2.0))


class KnowledgeBase:
    def __init__(self, project_root: Path | str):
        self.root = Path(os.path.abspath(project_root))
        self.kb_file = self.root / "config" / "knowledge_index.json"
        self.documents: List[Dict[str, Any]] = self._load_index()

    def _load_index(self) -> List[Dict[str, Any]]:
        if self.kb_file.exists():
            try:
                data = json.loads(self.kb_file.read_text(encoding="utf-8"))
                return data.get("documents", [])
            except Exception:
                pass
        return self._initialize_seed_knowledge()

    def _initialize_seed_knowledge(self) -> List[Dict[str, Any]]:
        seeds = [
            {
                "id": "doc-spec-01",
                "title": "Tool Build Processing & Sicherheits-Architektur",
                "source": "Tool Build Processing - Securty - So Baut man.txt",
                "category": "Architecture",
                "content": "8 Kern-Module: AppImage-Packaging, Caddy/NGINX Wildcard-DNS, Start-Vorhang mit WebAudio Glocke, 4s-Scheibenwischer, IAM Passkey/OTP Gate, KI-Suche, JMAP-Relay, Anonyme Telemetrie.",
                "dimension": 256,
                "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            },
            {
                "id": "doc-cert-02",
                "title": "Souveräne Zertifizierung & Daniel Pohl Identität",
                "source": "certificates/CERTIFICATION.md",
                "category": "Compliance",
                "content": "HCOS HNOSS Daniel Pohl, PIC 867679357, VAT 31353063511, DUNS 315676980, UNGM 1172700, Global LEI 894500GBJSIW8L6ET310, NATO Strategic Defense Alignment, EU Regulatory Governance.",
                "dimension": 256,
                "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            },
            {
                "id": "doc-mcp-03",
                "title": "Model Context Protocol & Externe Konnektoren",
                "source": "config/connectors.json",
                "category": "Integration",
                "content": "MCP Server Connector für GitHub Repository Analyse, Plaid Banking/Finanzdaten, Cloudflare DNS-Tunnel und n8n Workflow-Automatisierung.",
                "dimension": 256,
                "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
            }
        ]
        for doc in seeds:
            doc["vector"] = _pseudo_embedding(doc["content"], 256)
        self._save_index(seeds)
        return seeds

    def _save_index(self, docs: List[Dict[str, Any]]):
        self.kb_file.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "system": "HCOS FORINA KNOWLEDGE BASE",
            "version": "1.2.0",
            "total_documents": len(docs),
            "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "documents": docs
        }
        self.kb_file.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    def index_document(self, title: str, content: str, source: str = "custom", category: str = "general", dim: int = 256) -> Dict[str, Any]:
        doc_id = f"doc-{hashlib.md5(title.encode()).hexdigest()[:8]}"
        vector = _pseudo_embedding(content, dim)
        doc = {
            "id": doc_id,
            "title": title,
            "source": source,
            "category": category,
            "content": content,
            "dimension": dim,
            "vector": vector,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        self.documents.append(doc)
        self._save_index(self.documents)
        return doc

    def index_website_simulation(self, url: str, page_limit: int = 10, depth: int = 2, filter_pattern: str = "") -> Dict[str, Any]:
        """Simulates website crawling and indexing like in Mistral Studio."""
        domain = re.sub(r"^https?://", "", url).split("/")[0]
        title = f"Web-Index: {domain}"
        content = f"Indizierte Web-Dokumentation fuer {url}. Max Pages: {page_limit}, Tiefe: {depth}, Filter: '{filter_pattern}'. Relevante Compliance- und API-Punkte fuer automatisierte RAG-Abfragen strukturiert."
        doc = self.index_document(title=title, content=content, source=url, category="web-crawler")
        return {
            "status": "INDEXED",
            "url": url,
            "pages_analyzed": min(page_limit, 8),
            "doc_id": doc["id"],
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }

    def search(self, query: str, top_k: int = 3, dim: int = 256) -> List[Dict[str, Any]]:
        q_vec = _pseudo_embedding(query, dim)
        scored = []
        for doc in self.documents:
            sim = _cosine_similarity(q_vec, doc.get("vector", []))
            scored.append({
                "id": doc["id"],
                "title": doc["title"],
                "source": doc["source"],
                "category": doc["category"],
                "content": doc["content"],
                "score": round(sim * 100, 2)
            })
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]
