
"""Streamlit Frontend for Agentic Research Assistant"""

import sys
from pathlib import Path

import streamlit as st

# Make src importable
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.controller import ResearchController


st.set_page_config(
    page_title="Agentic Research Assistant",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 Agentic Research Assistant (CrewAI + Gemini + SerpAPI)")
st.write(
    """Ask any research question and a team of agents will:    1) search the web, 2) analyze sources, and 3) write a final answer."""
)

question = st.text_area(
    "Your research question",
    value="What are the main challenges in deploying large language models in healthcare?",    height=120,
)

if st.button("Run Research Pipeline"):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Agents are working on your question..."):
            controller = ResearchController(llm_model="gemini/gemini-2.0-flash")
            answer = controller.run_pipeline(question.strip())
        st.subheader("📄 Final Answer")
        st.write(answer)
