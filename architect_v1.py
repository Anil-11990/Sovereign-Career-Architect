import chromadb
import ollama

# 1. Connect to the Sovereign Memory
client = chromadb.PersistentClient(path="./sca_memory")
collection = client.get_or_create_collection(name="skill_dna")

def get_gap_analysis():
    print("--- [ARCHITECT: CALCULATING CAREER GAP] ---")

    # 2. Fetch Your Skills (Internal)
    # We filter by metadata we set in earlier days
    my_data = collection.get(where={"category": "Data Science"}) # Or whatever you tagged yours as
    my_skills = list(set(my_data['documents'])) # list(set()) removes duplicates

    # 3. Fetch Market Skills (External)
    market_data = collection.get(where={"source": "bridge_agent"})
    market_skills = list(set(market_data['documents']))

    print(f"Detected {len(my_skills)} Personal Skills.")
    print(f"Detected {len(market_skills)} Market Requirements.")

    # 4. The AI Judge
    prompt = f"""
    I have these skills: {', '.join(my_skills)}
    The market wants these skills: {', '.join(market_skills)}

    Analyze the gap. 
    1. Which high-demand market skills am I missing?
    2. Which of my current skills are most valuable?
    3. What is the ONE project I should build next to bridge the gap?
    
    Format the output as a clean Roadmap.
    """

    response = ollama.generate(model='phi3', prompt=prompt)
    print("\n" + "="*40)
    print("SOVEREIGN CAREER ROADMAP")
    print("="*40)
    print(response['response'])

if __name__ == "__main__":
    get_gap_analysis()