
from __future__ import annotations

import time
from typing import List, Dict

from .controller import ResearchController

TEST_QUERIES = [
    "What are the main challenges in deploying large language models in healthcare?",    "Compare reinforcement learning and supervised learning in terms of data requirements.",    "Summarize key trends in edge computing for IoT devices.",
]


def run_evaluation() -> List[Dict]:
    controller = ResearchController(llm_model="gemini/gemini-2.0-flash")

    results: List[Dict] = []
    for q in TEST_QUERIES:
        print("\n========================================")
        print(f"Question: {q}")
        print("========================================\n")
        start = time.time()
        answer = controller.run_pipeline(q)
        duration = time.time() - start
        print(answer)
        print(f"\n⏱️ Duration: {duration:.1f} seconds")
        results.append({
            "question": q,
            "answer": answer,
            "duration_sec": duration,
        })

    return results


if __name__ == "__main__":
    run_evaluation()
