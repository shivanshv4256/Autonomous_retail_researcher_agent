

from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = "sk-no-key"
os.environ["LLM_PROVIDER"] = "groq"
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

from crewai import Task, Crew

from agents.researcher import researcher
from agents.analyst import analyst
from agents.price_analyst import price_analyst
from agents.writer import writer

# user input
query = input("\nAsk your retail question: ")

# Tasks
research_task = Task(
    description=f"Research detailed market information about: {query}",
    expected_output="Detailed research findings",
    agent=researcher
)

analysis_task = Task(
    description="Analyze competitors based on the research findings",
    expected_output="Competitor analysis",
    agent=analyst,
    context=[research_task]
)

pricing_task = Task(
    description="Analyze pricing strategies using the competitor analysis",
    expected_output="Pricing strategy insights",
    agent=price_analyst,
    context=[analysis_task]
)

report_task = Task(
    description="Create final business report for the user",
    expected_output="Final professional report",
    agent=writer,
    context=[pricing_task]
)

# Crew workflow
crew = Crew(
    agents=[researcher, analyst, price_analyst, writer],
    tasks=[research_task, analysis_task, pricing_task, report_task],
    verbose=True
)

result = crew.kickoff()

print("\n========== FINAL REPORT ==========\n")
print(result)

