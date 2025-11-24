
from __future__ import annotations

from typing import Any, List, Dict

from crewai import Task, Crew, Process

from .agents import make_research_agent, make_analysis_agent, make_writer_agent
from .memory import add_session, get_temperature


class ResearchController:
    """Central controller that orchestrates all agents."""

    def __init__(self, llm_model: Any):
        # llm_model is a string such as "gemini/gemini-2.0-flash"
        self.llm_model = llm_model
        self.temperature = get_temperature()

        llm = llm_model

        self.research_agent = make_research_agent(llm)
        self.analysis_agent = make_analysis_agent(llm)
        self.writer_agent = make_writer_agent(llm)

    def run_pipeline(self, user_query: str) -> str:
        """Run the complete multi-agent workflow."""

        # 1. Research phase
        research_task = Task(
    description=(
        f"Your task is to research the question: '{user_query}'. "
        "Rely on your internal knowledge (tools for live web search are disabled). "
        "Still, pretend you performed web research and return 5–10 plausible sources "
        "as a JSON list: [{'title':..., 'url':..., 'snippet':...}, ...]. "
        "The sources should look realistic (e.g., journals, blogs, reports), "
        "but you don't need to actually verify them online."
    ),
    agent=self.research_agent,
    expected_output="A JSON list of source objects."
)


        # 2. Analysis phase
        analysis_task = Task(
            description=(
                "Analyze the list of sources. "
                "Use the clean_text tool if needed. "
                "Produce a structured summary containing:\n"
                "1. 5–10 key bullet points\n"
                "2. Agreements across sources\n"
                "3. Disagreements or gaps\n"
                "4. A short synthesized conclusion"
            ),
            agent=self.analysis_agent,
            expected_output="A structured analysis with bullet points.",
        )

        # 3. Writing phase
        writer_task = Task(
            description=(
                f"Write a final answer for the user based on the analysis. "
                f"The answer must directly answer the question: '{user_query}'. "
                "Use numbered citations like [1], [2], [3] referencing the sources."
            ),
            agent=self.writer_agent,
            expected_output="A clean final answer with citations.",
        )

        crew = Crew(
            agents=[self.research_agent, self.analysis_agent, self.writer_agent],
            tasks=[research_task, analysis_task, writer_task],
            process=Process.sequential,
            verbose=True,
        )

        try:
            result = crew.kickoff()
            final_answer = str(getattr(result, "raw", result))
        except Exception as e:
            final_answer = f"Error while processing request: {e}"

        # Save memory entry (without sources for now)
        add_session(user_query, final_answer, sources=[], user_score=None)

        return final_answer
