# 🛒 Autonomous Retail Intelligence System

An AI-powered **Multi-Agent Retail Research and Decision Support System** built using CrewAI, Groq LLaMA 3 70B, and Retrieval-Augmented Generation (RAG) with ChromaDB.

This system autonomously performs:

* Market Research
* Competitive Analysis
* Pricing Strategy Evaluation
* Structured Business Report Generation
* Persistent Memory Storage for Future Context

---

# 🚀 Features

* 🔎 Multi-Agent Architecture (Research → Analysis → Pricing → Reporting)
* 🧠 Retrieval-Augmented Generation (RAG)
* 💾 Persistent Vector Memory using ChromaDB
* ⚡ High-speed reasoning using LLaMA 3 70B via Groq
* 🌐 Web-based UI using Streamlit
* 📊 Structured Professional Business Reports
* 🔁 Cross-session Memory Retention

---

# 🏗 System Architecture

The system follows a **Multi-Agent RAG Architecture**:

1. User submits retail query via Streamlit.
2. System retrieves similar past reports from ChromaDB.
3. Retrieved context is injected into Research Agent.
4. Agents execute sequential workflow:

   * Research Agent
   * Analyst Agent
   * Price Analyst Agent
   * Report Writer Agent
5. Final report is generated using LLaMA 3 70B.
6. Report is stored back into ChromaDB for future retrieval.

---

# 🛠 Tech Stack

* CrewAI (Multi-Agent Orchestration)
* Groq API (LLM Provider)
* LLaMA 3 70B (Language Model)
* ChromaDB (Vector Database)
* Sentence Transformers (Embeddings)
* Streamlit (Frontend UI)
* LiteLLM (LLM Interface Layer)

---

# 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd Autonomous_Retail_Agent1
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If missing:

```bash
pip install apscheduler
```

---

# 🔑 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

# ▶️ Run Application

```bash
python -m streamlit run app.py
```

Then open browser at:

```
http://localhost:8501
```

---

# 🧠 How RAG Works in This Project

* Every generated report is converted into embeddings.
* Stored inside ChromaDB.
* On new query, system retrieves semantically similar reports.
* Retrieved memory is injected into Research Agent.
* This improves contextual reasoning and analytical accuracy.

---

# 📁 Project Structure

```
Autonomous_Retail_Agent1/
│
├── agents/
│   ├── researcher.py
│   ├── analyst.py
│   ├── price_analyst.py
│   └── writer.py
│
├── tools/
│   └── search_tool.py
│
├── vector_store.py
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

# 🎯 Key Outcomes

* Autonomous retail intelligence system
* Persistent semantic memory
* Structured business strategy generation
* Scalable modular multi-agent architecture

---

# 🔮 Future Enhancements

* Real-time API data integration
* Demand forecasting models
* Advanced data visualization dashboards
* Cloud deployment
* Multi-language support
* Export reports as PDF/Excel

---


