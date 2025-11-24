
# Agentic Research Assistant (CrewAI + Gemini)

This project is a minimal, working example of a multi-agent research assistant using
[CrewAI](https://github.com/crewAIInc/crewAI) and Google's Gemini models.

It exposes:
- A **CLI** entry point: `python -m src.main "your question"`
- A simple **Streamlit frontend**: `streamlit run frontend/app.py`

---

## 1. Installation

```bash
# 1) Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3) Install CrewAI's Gemini provider extras (if needed)
pip install "crewai[google-genai]"
```

---

## 2. Set your API keys

You need a Gemini API key from Google AI Studio.

Export it as an environment variable **before** running anything:

```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
# Optional but supported as well:
export GOOGLE_API_KEY="$GEMINI_API_KEY"
```

On Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
$env:GOOGLE_API_KEY=$env:GEMINI_API_KEY
```

---

## 3. Run from the command line

From the project root:

```bash
# Activate venv first if not already active
source venv/bin/activate  # or venv\Scripts\activate on Windows

python -m src.main "What are the main challenges in deploying large language models in healthcare?"
```

You should see CrewAI logs and finally:

```text
===== FINAL ANSWER =====

...assistant's answer here...
```

---

## 4. Run the evaluation script (multiple test queries)

```bash
python -m src.eval_runner
```

This will run the pipeline on several predefined questions and print duration for each.

---

## 5. Run the Streamlit frontend

```bash
streamlit run frontend/app.py
```

Then open the URL shown in the terminal (usually http://localhost:8501) and type
a research question in the text box.

---

## 6. Memory

Each run is appended to `run_memory.json` in the project root with the fields:

- `question`
- `answer`
- `sources` (currently empty, but you can extend controller to store them)
- `user_score` (placeholder for future feedback)

You can safely delete `run_memory.json` if you want to reset history.
