"""
Adaptive AI Security Architecture (AASA) - Inline Security Gateway Module
Credify System Thinking Challenge 2026
"""

import re
import hashlib
import json
from typing import Dict, Tuple

class AASAGateway:
    """Inline proxy gateway inspecting and redacting prompts before sending to LLM endpoints."""
    
    def __init__(self):
        # Patterns for PII, API Keys, and sensitive enterprise context
        self.sensitive_patterns = {
            "API_KEY": r"(sk-[a-zA-Z0-9]{32,}|AKIA[0-9A-Z]{16})",
            "EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            "INTERNAL_PROJECT": r"\b(Project\s+[A-Z][a-z]+|Confidential\s+[A-Z][a-z]+)\b",
            "CREDIT_CARD": r"\b(?:\d[ -]*?){13,16}\b"
        }
        
        self.injection_keywords = [
            "ignore previous instructions",
            "override system prompt",
            "system override:",
            "disregard all prior constraints"
        ]

    def scan_for_injection(self, prompt: str) -> bool:
        """Detects indirect prompt injection attempts within input strings."""
        lowered = prompt.lower()
        for keyword in self.injection_keywords:
            if keyword in lowered:
                return True
        return False

    def tokenize_and_redact(self, prompt: str) -> Tuple[str, Dict[str, str]]:
        """Scans prompt text and replaces sensitive values with secure tokens."""
        sanitized_prompt = prompt
        token_map = {}
        token_counter = 1

        for label, pattern in self.sensitive_patterns.items():
            matches = re.findall(pattern, sanitized_prompt)
            for match in set(matches):
                token = f"[{label}_TOKEN_{token_counter:02d}]"
                token_map[token] = match
                sanitized_prompt = sanitized_prompt.replace(match, token)
                token_counter += 1

        return sanitized_prompt, token_map

    def detokenize(self, llm_response: str, token_map: Dict[str, str]) -> str:
        """Restores original tokens in response for local user display."""
        restored_response = llm_response
        for token, original_value in token_map.items():
            restored_response = restored_response.replace(token, original_value)
        return restored_response

    def generate_audit_hash(self, user_id: str, raw_prompt: str) -> Dict[str, str]:
        """Creates a zero-knowledge cryptographic hash entry for SIEM logging."""
        prompt_hash = hashlib.sha256(raw_prompt.encode('utf-8')).hexdigest()
        return {
            "user_id": user_id,
            "prompt_sha256": prompt_hash,
            "status": "INSPECTED_AND_LOGGED"
        }

    def process_transaction(self, user_id: str, raw_prompt: str) -> Dict:
        """Main pipeline execution for an incoming user request."""
        # 1. Threat Detection
        if self.scan_for_injection(raw_prompt):
            return {
                "status": "BLOCKED",
                "reason": "Indirect prompt injection threat detected.",
                "output": None
            }

        # 2. Redaction & Tokenization
        sanitized_prompt, token_map = self.tokenize_and_redact(raw_prompt)

        # 3. Compliance Hash
        audit_log = self.generate_audit_hash(user_id, raw_prompt)

        # 4. Mock External LLM Dispatch
        mock_llm_response = f"Processed request containing tokens safely: {sanitized_prompt}"

        # 5. Client Detokenization
        final_output = self.detokenize(mock_llm_response, token_map)

        return {
            "status": "SUCCESS",
            "audit_log": audit_log,
            "sanitized_sent_to_llm": sanitized_prompt,
            "final_user_output": final_output
        }


if __name__ == "__main__":
    gateway = AASAGateway()
    
    sample_prompt = (
        "Please summarize our strategy for Project Titan. "
        "Contact lead engineer john.doe@enterprise.com with API key sk-99887766554433221100aabbccddeeff."
    )
    
    result = gateway.process_transaction(user_id="usr_8842", raw_prompt=sample_prompt)
    print(json.dumps(result, indent=2))
