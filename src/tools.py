
from __future__ import annotations

from typing import List, Dict, Any

from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileReadTool
from crewai.tools import tool
# 1) Web search tool (Serper)
#    Requires SERPER_API_KEY in your environment.
search_tool = SerperDevTool()

# 2) Website scraper
scrape_tool = ScrapeWebsiteTool()

# 3) File reader (for local notes / PDFs)
file_tool = FileReadTool()


@tool
def clean_text(text: str) -> str:
    """Clean raw text by removing extra whitespace.

    This is a very simple implementation just to demonstrate a custom tool.
    Agents can call this to post-process scraped content.
    """
    if not isinstance(text, str):
        return str(text)
    # Collapse repeated whitespace and strip edges
    import re
    cleaned = re.sub(r"\s+", " ", text).strip()
    return cleaned
