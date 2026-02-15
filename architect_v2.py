import chromadb
import ollama

client = chromadb.PersistentClient(path="./sca_memory")
collection = client.get_or_create_collection(name="skill_dna")

def get_markdown_roadmap():
    print("--- [ARCHITECT: GENERATING MARKDOWN ROADMAP] ---")

    # Fetch data (Ensure these tags match your bridge_v1.py and ledger_v1.py)
    my_data = collection.get(where={"category": "Data Science"})
    market_data = collection.get(where={"source": "bridge_agent"})
    
    my_skills = list(set(my_data['documents']))
    market_skills = list(set(market_data['documents']))

    # The "Markdown" Prompt
    prompt = f"""
    You are a Senior Career Strategist. Analyze the gap between these two lists.
    
    MY SKILLS: {', '.join(my_skills)}
    MARKET DEMAND: {', '.join(market_skills)}

    Generate a report strictly in MARKDOWN format using the following structure:
    # SCA Career Strategy Report
    ## 1. Skill Gap Analysis
    (List missing skills here using bullet points)
    
    ## 2. Competitive Advantage
    (List which of my current skills are most 'in-demand' based on the market list)
    
    ## 3. The 'Blast' Project
    (Describe one specific, high-level project I should build to bridge the gap)
    
    ### Action Plan
    | Phase | Task | Duration |
    | :--- | :--- | :--- |
    | 1 | Skill Acquisition | 2 Weeks |
    | 2 | Project Build | 4 Weeks |
    """

    # Replace 'phi3' with your working model name
    response = ollama.generate(model='phi3', prompt=prompt)
    
    # Save the output to a file so you can see the Markdown
    with open("Career_Roadmap.md", "w") as f:
        f.write(response['response'])
    
    print("\n✅ SUCCESS: Roadmap saved to 'Career_Roadmap.md'")
    print("Open this file in VS Code and press 'Ctrl+Shift+V' to see it formatted!")

if __name__ == "__main__":
    get_markdown_roadmap()