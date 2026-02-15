import chromadb

# 1. Setup Persistent Storage (The 'Safe' on your disk)
# This creates a folder called 'sca_memory' where your data stays forever.
client = chromadb.PersistentClient(path="./sca_memory")

# 2. Create a Collection (Like a Table in a database)
# We call it 'skill_dna'
collection = client.get_or_create_collection(name="skill_dna")

def save_skill(id, skill_text, category):
    # This adds a skill to your permanent ledger
    collection.add(
        documents=[skill_text],
        metadatas=[{"category": category}],
        ids=[id]
    )
    print(f"✅ Skill Saved: {id}")

def query_skills(search_term):
    # This searches your brain for meaning
    results = collection.query(
        query_texts=[search_term],
        n_results=2
    )
    return results

# --- TEST IT ---
if __name__ == "__main__":
    # Day 2 Test: Saving your project experience
    #save_skill("proj_001", "Built a music recommendation system using Python and K-Means clustering", "Data Science")
    #save_skill("proj_002", "Developed a Flask API for user authentication and session management", "Web Dev")

    # Now, let's see if it remembers
    print("\nSearching for 'Machine Learning'...")
    memory = query_skills("Machine Learning")
    print(f"Found match: {memory['documents'][0][0]}")

def check_everything():
    print("\n--- [DATABASE AUDIT] ---")
    # .get() without arguments returns all IDs, metadatas, and documents
    all_data = collection.get()
    
    if not all_data['ids']:
        print("The ledger is empty!")
    else:
        for i in range(len(all_data['ids'])):
            print(f"ID: {all_data['ids'][i]}")
            print(f"Content: {all_data['documents'][i]}")
            print(f"Metadata: {all_data['metadatas'][i]}")
            print("-" * 20)

# Call the function to see the results
check_everything()