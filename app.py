import streamlit as st
from crewai import Task, Crew
from agents.researcher import researcher
from agents.analyst import analyst
from agents.price_analyst import price_analyst
from agents.writer import writer
from vector_store import store_report, search_similar_reports


st.set_page_config(
    page_title="Autonomous Retail Intelligence",
    page_icon="🛒",
    layout="wide"
)


st.markdown("""
    <style>
    .main-title {
        font-size: 38px;
        font-weight: bold;
        color: #2E86C1;
    }
    .sub-text {
        font-size: 18px;
        color: #555;
    }
    .report-box {
        background-color: #F4F6F7;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #D5DBDB;
    }
    </style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.header("⚙ System Info")
    st.write("Model: LLaMA 3 70B (Groq)")
    st.write("Architecture: Multi-Agent + RAG")
    st.write("Vector DB: ChromaDB")
    st.success("Memory Enabled")


st.markdown('<div class="main-title">🛒 Autonomous Retail Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">AI-powered retail market research using Multi-Agent RAG system</div>', unsafe_allow_html=True)
st.divider()


query = st.text_input("🔎 Enter your retail market question:")

if st.button("🚀 Analyze Market"):

    if not query:
        st.warning("Please enter a market question.")
    else:
        with st.spinner("🤖 AI Agents are analyzing market data..."):

            
            similar_reports = search_similar_reports(query)

            memory_context = ""
            if similar_reports and similar_reports[0]:
                memory_context = "\n".join(similar_reports[0])

            
            research_task = Task(
                description=f"""
                User Question: {query}

                Relevant Past Reports:
                {memory_context}

                Use past insights only if relevant.
                Provide key market facts.
                """,
                expected_output="Bullet insights",
                agent=researcher
            )

            analysis_task = Task(
                description="Analyze competitors and extract key trends.",
                expected_output="Competitive analysis",
                agent=analyst,
                context=[research_task]
            )

            pricing_task = Task(
                description="Provide pricing strategy recommendations.",
                expected_output="Pricing insights",
                agent=price_analyst,
                context=[analysis_task]
            )

            report_task = Task(
                description="""
                Generate final report including:
                - Executive Summary
                - Key Market Trends
                - Competitive Insights
                - Pricing Strategy
                - Strategic Recommendations
                """,
                expected_output="Structured professional report",
                agent=writer,
                context=[pricing_task]
            )

            crew = Crew(
                agents=[researcher, analyst, price_analyst, writer],
                tasks=[research_task, analysis_task, pricing_task, report_task],
                verbose=False
            )

            result = crew.kickoff()
            result_text = result.raw if hasattr(result, "raw") else str(result)

            
            store_report(result_text)

        
        st.success("✅ Analysis Completed!")


        st.markdown("### 📊 Retail Intelligence Report")
        st.markdown(result_text)

        st.info("🧠 Report stored in memory for future retrieval.")