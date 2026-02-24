from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0)

analyst = Agent(
    role="Retail Market Analyst",
    goal="Analyze competitors and market positions",
    backstory="Expert in understanding brand strategies, strengths and weaknesses in retail industry",
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=2
)