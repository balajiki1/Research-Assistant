
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

# Simple JSON-based memory store for past runs
PROJECT_ROOT = Path(__file__).parent.parent
MEMORY_PATH = PROJECT_ROOT / "run_memory.json"


def _load_memory() -> List[Dict[str, Any]]:
    if not MEMORY_PATH.exists():
        return []
    try:
        with MEMORY_PATH.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def _save_memory(data: List[Dict[str, Any]]) -> None:
    MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    with MEMORY_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def add_session(question: str,
                answer: str,
                sources: Optional[List[Dict[str, Any]]] = None,
                user_score: Optional[float] = None) -> None:
    """Append a single run to memory file."""
    data = _load_memory()
    data.append({
        "question": question,
        "answer": answer,
        "sources": sources or [],
        "user_score": user_score,
    })
    _save_memory(data)


def get_temperature() -> float:
    """Return default temperature for the LLM.

    You can later make this dynamic (e.g., based on past runs).
    """
    return 0.2
