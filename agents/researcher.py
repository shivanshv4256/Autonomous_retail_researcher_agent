

from crewai import Agent, LLM
from dotenv import load_dotenv
from tools.search_tool import InternetSearchTool

load_dotenv()


llm = LLM(
    model="groq/llama-3.3-70b-versatile",temperature=0
)

researcher = Agent(
    role="Retail Market Researcher",
    goal="Find latest retail market trends and competitor strategies",
    backstory="Professional",
    tools=[InternetSearchTool()],
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=2
)