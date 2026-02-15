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
<img width="1919" height="726" alt="Screenshot 2026-02-15 231213" src="https://github.com/user-attachments/assets/c2cfd5bc-5e6f-4706-aa63-99861f438755" />
<img width="1907" height="897" alt="Screenshot 2026-02-15 231309" src="https://github.com/user-attachments/assets/271a714c-2a31-4342-9632-b329287d2c7b" />

---

*Built by [Anil khanal] as part of the  AI Agent Challenge.*
