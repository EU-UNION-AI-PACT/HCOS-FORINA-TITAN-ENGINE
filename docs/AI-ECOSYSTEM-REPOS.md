# 🌟 HCOS FORINA TITAN — AI & MULTI-AGENT REPOSITORY ECOSYSTEM

Diese Übersicht ordnet allen aus der Mistral-Studio- und Multi-Agenten-Architektur identifizierten Modulen die führenden Open-Source GitHub-Repositories zu:

---

## 1. Model Context Protocol (MCP) & Konnektoren
| Modul | Offizielles GitHub Repository | Zweck in HCOS FORINA TITAN |
|---|---|---|
| **MCP Python SDK** | [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | Standardisierte Anbindung von Tools, Ressourcen und Prompts nach dem Anthropic/Open-Source MCP-Standard. |
| **MCP Reference Servers** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Vorgefertigte Konnektoren für GitHub, Filesystem, PostgreSQL, SQLite und Slack. |

---

## 2. Mistral AI & LLM Provider Gateway
| Modul | Offizielles GitHub Repository | Zweck in HCOS FORINA TITAN |
|---|---|---|
| **Mistral Python Client** | [mistralai/client-python](https://github.com/mistralai/client-python) | Offizieller Python-Client für Mistral Chat Completions, Embeddings und Agents. |
| **Mistral Common** | [mistralai/mistral-common](https://github.com/mistralai/mistral-common) | Tokenizer, Tool-Calling-Schemas und Validierungslogik für Mistral-Modelle. |
| **Ollama (Local Offline)** | [ollama/ollama](https://github.com/ollama/ollama) | Völlig autarkes, lokales Ausführen von Open-Source LLMs (Mistral 7B, Llama 3) ohne Cloud-Abhängigkeit. |

---

## 3. Multi-Agenten-Orchestrierung & Skill-System
| Modul | Offizielles GitHub Repository | Zweck in HCOS FORINA TITAN |
|---|---|---|
| **LangGraph** | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Zyklische, zustandsbehaftete Graphen für koordinierte Multi-Agenten-Workflows. |
| **AutoGen** | [microsoft/autogen](https://github.com/microsoft/autogen) | Kollaboratives Multi-Agenten-Framework von Microsoft für autonomes Coding und Review. |
| **LlamaIndex** | [run-llama/llama_index](https://github.com/run-llama/llama_index) | RAG-Pipeline zur Verbindung strukturierter Wissensquellen mit Agenten. |

---

## 4. Website-Indizierung, Crawler & Vektorsuche
| Modul | Offizielles GitHub Repository | Zweck in HCOS FORINA TITAN |
|---|---|---|
| **Firecrawl** | [mendableai/firecrawl](https://github.com/mendableai/firecrawl) | Wandelt ganze Websites (inkl. Subseiten) per URL-Crawler direkt in sauberes LLM-Markdown um (wie im Mistral Studio Web-Indexer). |
| **Crawlee Python** | [apify/crawlee-python](https://github.com/apify/crawlee-python) | Schneller, robuster Web-Crawler von Apify für tiefe Website-Indizierungen. |
| **ChromaDB** | [chroma-core/chroma](https://github.com/chroma-core/chroma) | Schlanke, lokale Open-Source Vektordatenbank für Embeddings (128, 256, 1024 Dimensionen). |
| **Qdrant** | [qdrant/qdrant](https://github.com/qdrant/qdrant) | Hochperformante Vektor-Suchmaschine für große Wissensdatenbanken. |

---

## 5. Spracheingabe (STT) & Sprachausgabe (TTS)
| Modul | Offizielles GitHub Repository | Zweck in HCOS FORINA TITAN |
|---|---|---|
| **Whisper (STT)** | [openai/whisper](https://github.com/openai/whisper) | Hochpräzise Offline-Spracherkennung für Sprachbefehle im Cockpit. |
| **Coqui TTS** | [coqui-ai/TTS](https://github.com/coqui-ai/TTS) | Lokale Deep-Learning Sprachsynthese zur Audioausgabe von Prüfberichten. |

---

## 6. Finanz-, Automatisierungs- & Workflow-Konnektoren
| Modul | Offizielles GitHub Repository | Zweck in HCOS FORINA TITAN |
|---|---|---|
| **n8n** | [n8n-io/n8n](https://github.com/n8n-io/n8n) | Selbst gehostete Workflow-Automatisierung mit hunderten Konnektoren. |
| **Plaid Python** | [plaid/plaid-python](https://github.com/plaid/plaid-python) | Offizielle API-Bibliothek zur sicheren Anbindung von Bankkonten und Finanztransaktionen. |
