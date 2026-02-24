from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0)

writer = Agent(
    role="Business Report Writer",
    goal="Create a clear final report combining all analysis",
    backstory="Professional consultant who writes executive business reports",
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=2
)