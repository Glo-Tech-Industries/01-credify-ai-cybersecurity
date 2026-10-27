# Adaptive AI Security Architecture (AASA): Pitch Deck Script
> Credify System Thinking Challenge 2026

## Slide 1: Title Slide
* **Headline:** Securing Enterprise GenAI Without Breaking Workflow.
* **Sub-text:** Introducing AASA: The Inline Zero-Trust Security Proxy.

## Slide 2: The Problem (Shadow IT & Friction)
* Employees want LLM speed; security teams want data protection.
* Hard perimeter blocks lead straight to unmanaged shadow tools.

## Slide 3: The Root Cause
* Traditional perimeter security can't inspect conversational context or fluid natural language payloads.

## Slide 4: Introducing AASA
* An inline, zero-trust context proxy that sits right between users and external LLM APIs.

## Slide 5: Core Feature 1 — PII Redaction
* Automatically catches API keys, emails, and sensitive project names, swapping them for secure local tokens.

## Slide 6: Core Feature 2 — Injection Scanning
* Blocks indirect prompt injections before malicious payloads execute.

## Slide 7: Core Feature 3 — Cryptographic SIEM Logging
* Generates SHA-256 transaction hashes for bulletproof compliance without storing plain-text private data offsite.

## Slide 8: Client-Side Detokenization
* Restores original tokens seamlessly on the user's end so output reads naturally.

## Slide 9: Architecture & Data Flow
* Zero-friction pipeline running in under 15ms of latency overhead.

## Slide 10: System Thinking & Trade-offs
* Balancing maximum enterprise protection with smooth developer experience.

## Slide 11: Validation & Testing
* Fully covered by automated unit tests safeguarding redaction and injection blocks.

## Slide 12: Conclusion & Next Steps
* Scaling AASA for enterprise-wide deployment. Thank you!
