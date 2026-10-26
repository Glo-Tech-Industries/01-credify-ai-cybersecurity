# Adaptive AI Security Architecture (AASA)
> **Credify System Thinking Challenge 2026 — Challenge 01: AI & Cybersecurity**

## Overview
As enterprises adopt generative AI, traditional perimeter defenses fail to inspect non-deterministic natural language payloads. **AASA** is an inline, zero-trust context proxy that redacts sensitive PII, API tokens, and corporate IP in real-time before prompts reach third-party LLM endpoints, detokenizing output upon receipt.

---

## Key Features
* **Context-Aware Named Entity Redaction:** Intercepts sensitive entities using local NLP model rules.
* **Indirect Prompt Injection Scanning:** Filters malicious embedded directives inside prompt payloads.
* **Zero-Knowledge SIEM Hashing:** Generates cryptographic hashes for compliance logging without offsite plain-text storage.
* **Client-Side Detokenization:** Transparently restores context for the end user.

---

## Project Structure
```text
.
├── README.md                           # Overview & setup instructions
├── docs/
│   ├── ARCHITECTURE_DOCUMENTATION.md   # Full project report & systems analysis
│   └── PITCH_DECK_SLIDES.md            # 12-slide competition pitch deck script
├── src/
│   └── gateway_proxy.py                # Core Python prototype implementation
├── tests/
│   └── test_gateway.py                # Validation unit tests
└── requirements.txt                    # Project dependencies
