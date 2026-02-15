import ollama
import chromadb
import uuid # This generates a unique ID for every skill

# 1. Connect to our Memory (Day 2)
client = chromadb.PersistentClient(path="./sca_memory")
collection = client.get_or_create_collection(name="skill_dna")

def bridge_process(project_description):
    print(f"\n--- [AGENT START: ANALYZING PROJECT] ---")
    
    # 2. Ask the Librarian to extract skills in a specific format
    # We ask for a comma-separated list to make it easy to split
    # Use this stricter prompt
    prompt = f"List only the technical skills found in this text, separated by commas. Do not include introductory text or explanations. Text: {project_description}"
    
    response = ollama.generate(model='phi3', prompt=prompt)
    skills_extracted = response['response'].strip()
    
    print(f"Librarian found: {skills_extracted}")

    # 3. Save each skill into the Ledger
    # We split the string by commas and save them one by one
    skill_list = skills_extracted.split(',')
    
    for skill in skill_list:
        skill_clean = skill.strip()
        if skill_clean:
            unique_id = str(uuid.uuid4())[:8] # Generates a short random ID
            collection.add(
                documents=[skill_clean],
                metadatas=[{"source": "bridge_agent"}],
                ids=[unique_id]
            )
            print(f"✅ Saved to Ledger: {skill_clean} (ID: {unique_id})")

if __name__ == "__main__":
    # Correct way: wrap the whole sentence in quotes!
    my_work = "I optimized a PostgreSQL database by implementing indexing and query caching, reducing latency by 40%."
    bridge_process(my_work)