import chromadb

# Connect to the same folder you created
client = chromadb.PersistentClient(path="./sca_memory")

# Get the collection
collection = client.get_or_create_collection(name="skill_dna")

def show_me_everything():
    print("\n" + "="*30)
    print("SCA LEDGER: DATABASE AUDIT")
    print("="*30)
    
    # This pulls every single record stored
    data = collection.get()
    
    # Check if there is actually data
    count = len(data['ids'])
    print(f"TOTAL RECORDS FOUND: {count}\n")
    
    if count == 0:
        print("❌ DATABASE IS EMPTY.")
        print("Run ledger_v1.py first to save data!")
    else:
        for i in range(count):
            print(f"[{i+1}] ID: {data['ids'][i]}")
            print(f"    SKILL: {data['documents'][i]}")
            print(f"    TAGS:  {data['metadatas'][i]}")
            print("-" * 30)

if __name__ == "__main__":
    show_me_everything()