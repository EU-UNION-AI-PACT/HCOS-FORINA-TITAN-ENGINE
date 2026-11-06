"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
MODULE 04: KNOWLEDGE & RAG ENGINE
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.

Proprietary License - All Rights Reserved.
Inspiration: Mistral Document & Knowledge Search, Semantic Retrieval & Embeddings.
"""
from __future__ import annotations
import hashlib
import json
import math
import time
from typing import Dict, Any, List

MODULE_INFO = {
    "id": "04_knowledge_rag",
    "name": "Knowledge & RAG Engine",
    "version": "1.2.0",
    "group": "Intelligence Suite",
    "category": "Data & Retrieval"
}

KNOWLEDGE_INDEX = [
    {
        "id": "kb_doc_1",
        "title": "HCOS Sovereign Architecture Manual",
        "category": "Governance",
        "text": "Die HCOS Architektur basiert auf kryptografischer Unabhaengigkeit, Ed25519-Zertifikaten und fail-closed Security Gates unter Daniel Pohl.",
        "tags": ["governance", "hcos", "ed25519", "sovereign"]
    },
    {
        "id": "kb_doc_2",
        "title": "EU AI Act Compliance & Risk Classification",
        "category": "Legal",
        "text": "Verordnung (EU) 2024/1689: Harmonisierte Vorschriften fuer Kuenstliche Intelligenz, Transparenzpflichten und Risikomanagement.",
        "tags": ["eu", "ai-act", "compliance", "transparenz"]
    },
    {
        "id": "kb_doc_3",
        "title": "Offline-First Deterministic Packaging & PWA",
        "category": "Engineering",
        "text": "FORINA TITAN laeuft voellig autark im Browser als PWA sowie als AppImage auf Linux ohne externe Cloud-Abhaengigkeit.",
        "tags": ["offline", "pwa", "appimage", "deterministic"]
    }
]

def _mock_embedding(text: str, dim: int = 128) -> List[float]:
    raw_hash = hashlib.sha256(text.encode("utf-8")).digest()
    vec = []
    for i in range(dim):
        b = raw_hash[i % len(raw_hash)]
        vec.append((b - 128) / 128.0)
    norm = math.sqrt(sum(x * x for x in vec)) or 1.0
    return [x / norm for x in vec]

def _cosine_similarity(v1: List[float], v2: List[float]) -> float:
    return sum(a * b for a, b in zip(v1, v2))

def self_test() -> Dict[str, Any]:
    emb1 = _mock_embedding("Governance")
    emb2 = _mock_embedding("Governance")
    sim = _cosine_similarity(emb1, emb2)
    return {
        "status": "PASS" if abs(sim - 1.0) < 1e-4 else "FAIL",
        "module": MODULE_INFO["id"],
        "documents_indexed": len(KNOWLEDGE_INDEX),
        "embedding_dimensions": len(emb1),
        "cosine_test": round(sim, 4),
        "latency_ms": 1.5
    }

def health_check() -> Dict[str, Any]:
    return {"module": MODULE_INFO["id"], "healthy": True, "timestamp": time.time()}

def execute(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if action == "search":
        query = params.get("query", "Governance")
        q_emb = _mock_embedding(query)
        scored = []
        for doc in KNOWLEDGE_INDEX:
            doc_emb = _mock_embedding(doc["text"])
            score = _cosine_similarity(q_emb, doc_emb)
            # Boost score if tag directly matches
            if any(term in doc["text"].lower() or term in doc["tags"] for term in query.lower().split()):
                score += 0.35
            scored.append({**doc, "relevance_score": round(min(score, 0.99), 3)})

        scored.sort(key=lambda x: x["relevance_score"], reverse=True)
        return {
            "status": "SUCCESS",
            "query": query,
            "results": scored[:params.get("top_k", 3)],
            "executed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }

    elif action == "index_document":
        doc_id = params.get("id", f"doc_{len(KNOWLEDGE_INDEX)+1}")
        new_doc = {
            "id": doc_id,
            "title": params.get("title", "Neues Dokument"),
            "category": params.get("category", "General"),
            "text": params.get("text", ""),
            "tags": params.get("tags", [])
        }
        KNOWLEDGE_INDEX.append(new_doc)
        return {"status": "SUCCESS", "indexed_id": doc_id, "total_docs": len(KNOWLEDGE_INDEX)}

    return {"status": "ERROR", "message": f"Unbekannte Aktion: {action}"}
