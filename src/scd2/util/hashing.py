"""Hashing utilities."""

import json
from hashlib import sha256


def stable_hash(attrs: dict) -> str:
    """Compute a deterministic hash of attribute dictionary."""
    return sha256(json.dumps(attrs, sort_keys=True).encode()).hexdigest()
