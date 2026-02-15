# 🚀 Sovereign Career Architect (SCA)

**An autonomous AI Agent that tracks my skills, scouts the job market, and generates career strategy roadmaps.**

## 🤖 The Architecture
This project uses a multi-agent system running entirely locally:
1.  **The Librarian:** Uses `Ollama (Phi-3)` to extract skills from project descriptions.
2.  **The Ledger:** Stores career DNA in a `ChromaDB` vector database.
3.  **The Scout:** Scrapes job boards using `BeautifulSoup` to analyze market demand.
4.  **The Architect:** Performs gap analysis and generates learning roadmaps.

## 🛠️ Tech Stack
* **Python 3.9+**
* **Streamlit** (Frontend Dashboard)
* **Ollama** (Local LLM Inference)
* **ChromaDB** (Vector Memory)
* **BeautifulSoup4** (Web Scraping)

## 🚀 How to Run
1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Ensure Ollama is running: `ollama serve`
4.  Launch the dashboard: `streamlit run dashboard_v2.py`

## 📸 Screenshots
*(You will add screenshots here later)*

---
*Built by [Anil khanal] as part of the 7-Day AI Agent Challenge.*