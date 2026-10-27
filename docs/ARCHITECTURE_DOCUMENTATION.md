# Adaptive AI Security Architecture (AASA): Technical Report & System Design
> Credify System Thinking Challenge 2026 - Challenge 01

## 1. Problem Statement & System Framing
Traditional enterprise AI policies often rely on hard perimeter blocks, forcing employees to use unmanaged shadow devices or personal accounts to access generative tools. AASA solves this by providing an inline, transparent security proxy that operates at the API layer, removing the friction that drives shadow IT.

---

## 2. Stakeholders & Incentive Analysis
* **Employees / End Users:** Desire fast, unrestricted access to generative AI tools for productivity. Incentivized to bypass rigid corporate bans if tools are too slow or restrictive.
* **Security & Compliance Teams:** Accountable for preventing data leaks (PII/IP) and mitigating prompt injection vulnerabilities. Incentivized to lock down access, often creating friction.
* **AASA Alignment:** Aligns both parties by offering automated, zero-friction protection that keeps employees compliant without sacrificing productivity.

---

## 3. Root Causes & System Relationships
* **Visible Symptom:** Data exfiltration and accidental PII leakage through third-party LLM prompts.
* **Root Cause:** A mismatch between non-deterministic conversational interfaces and rigid, perimeter-based legacy security models. Because natural language payloads are fluid, static firewalls cannot inspect context.

---

## 4. Architectural Overview & Data Flow
AASA intercepts incoming prompts before they reach external LLM endpoints, executing four core stages synchronously:
1. **Threat Scanning:** Evaluates prompt text against known indirect prompt injection signatures.
2. **Context-Aware Redaction:** Matches and replaces sensitive PII, internal project names, and API keys with secure pseudo-random tokens.
3. **Cryptographic Auditing:** Generates an immutable SHA-256 hash of the transaction for zero-knowledge compliance logging.
4. **Client-Side Detokenization:** Restores original context on the user's end upon receiving the LLM response.

```text
[User Prompt] 
    ↓ (Inline Interception)
[AASA Gateway Proxy] 
    ├── 1. Injection Check (Blocks if malicious)
    ├── 2. Regex / NER Redaction (Replaces PII with [TOKEN_XX])
    └── 3. SIEM Audit Logging (Stores SHA-256 hash)
    ↓ (Sanitized Payload)
[External LLM Endpoint]
    ↓ (Response with Tokens)
[Client-Side Detokenization] 
    ↓ (Original Context Restored)
[End User]
