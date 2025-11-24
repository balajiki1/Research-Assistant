
from __future__ import annotations

import argparse

from .controller import ResearchController


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Agentic Research Assistant (CrewAI demo)."
    )
    parser.add_argument(
        "question",
        type=str,
        nargs="*",        help="Research question to ask the agentic system.",
    )
    args = parser.parse_args()

    if not args.question:
        print("Please provide a question, e.g.:");
        print("  python -m src.main \"What are the risks of AI in finance?\"")
        return

    question = " ".join(args.question)
    # ✅ Use a valid Gemini model name
    controller = ResearchController(llm_model="gemini/gemini-2.0-flash")
    answer = controller.run_pipeline(question)
    print("\n===== FINAL ANSWER =====\n")
    print(answer)


if __name__ == "__main__":
    main()
