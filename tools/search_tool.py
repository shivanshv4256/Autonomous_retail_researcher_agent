
from crewai.tools import BaseTool
from duckduckgo_search import DDGS


class InternetSearchTool(BaseTool):
    name: str = "internet_search"
    description: str = "Search the internet for latest information about retail market trends,prices and sales number for latest 2025 "

    def _run(self, query: str) -> str:
        results_text = []

        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)

            for r in results:
                results_text.append(r["body"])

        return "\n".join(results_text)