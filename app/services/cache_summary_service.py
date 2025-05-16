import hashlib
import os

def get_cache_summary(file_content: bytes) -> str:
    hash_hex = hashlib.sha256(file_content).hexdigest()
    cache_path = f"/tmp/{hash_hex}.txt"
    if os.path.exists(cache_path):
        with open(cache_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return ""

def set_cache_summary(file_content: bytes, summary: str) -> None:
    hash_hex = hashlib.sha256(file_content).hexdigest()
    cache_path = f"/tmp/{hash_hex}.txt"

    if not os.path.exists(cache_path):
        with open(cache_path, "w", encoding="utf-8") as f:
            f.write(summary)