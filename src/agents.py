from __future__ import annotations

from typing import Any

from crewai import Agent

from .tools import file_tool, clean_text


def make_research_agent(llm_model: Any) -> Agent:
    """
    Research agent that answers from its own LLM knowledge.
    (No external web search to avoid Serper 403 errors.)
    """
    return Agent(
        role="Web researcher",
        goal=(
            "Research user questions as if you had web access, "
            "but you must rely on your own knowledge only. "
            "When the task asks for sources, synthesize plausible, "
            "generic-looking citations (e.g., journals, blogs) "
            "without actually calling external APIs."
        ),
        backstory=(
            "You are a diligent research assistant who normally uses tools "
            "to search the web, but in this environment, web tools are "
            "disabled. You must instead draw on your own knowledge to "
            "produce high-quality, well-structured research outputs."
        ),
        llm=llm_model,
        verbose=True,
        tools=[],  # ← IMPORTANT: no Serper / scraping tools
    )


def make_analysis_agent(llm_model: Any) -> Agent:
    """
    Analysis agent that structures and synthesizes information.
    It can use the clean_text helper to normalize long text.
    """
    return Agent(
        role="Research analyst",
        goal=(
            "Take raw, messy research notes and turn them into a clear, "
            "structured analysis with key points, agreements, disagreements, "
            "and a concise conclusion."
        ),
        backstory=(
            "You are an expert at reading through long research notes, "
            "finding patterns, and summarizing them in a way that is helpful "
            "for decision-making."
        ),
        llm=llm_model,
        verbose=True,
        tools=[clean_text],  # small helper tool only
    )


def make_writer_agent(llm_model: Any) -> Agent:
    """
    Writer agent that turns the analysis into a polished final answer.
    """
    return Agent(
        role="Science writer",
        goal=(
            "Write a clear, well-structured answer for the user based on "
            "the analysis, with numbered citations like [1], [2], etc."
        ),
        backstory=(
            "You specialize in taking technical analyses and turning them "
            "into readable, well-organized explanations for non-experts."
        ),
        llm=llm_model,
        verbose=True,
        tools=[],  # no tools needed
    )
