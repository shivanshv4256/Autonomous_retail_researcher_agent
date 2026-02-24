from crewai import Agent, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0)

price_analyst = Agent(
    role="Retail Pricing Strategist",
    goal="Analyze pricing strategies and discount patterns",
    backstory="Specialist in pricing psychology, offers and profit optimization",
    llm=llm,
    verbose=True,
    allow_delegation=False,
    max_iter=2
)