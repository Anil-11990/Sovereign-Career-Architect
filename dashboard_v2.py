import streamlit as st
import chromadb
import ollama
from bridge_v1 import bridge_process

# --- DATABASE SETUP ---
client = chromadb.PersistentClient(path="./sca_memory")
collection = client.get_or_create_collection(name="skill_dna")

# --- UI LAYOUT ---
st.set_page_config(page_title="SCA Command Center", layout="wide")
st.title("🚀 Sovereign Career Architect")

# --- SIDEBAR ---
all_data = collection.get()
st.sidebar.header("Skill DNA Stats")
st.sidebar.write(f"Total Skills Logged: **{len(all_data['ids'])}**")

# --- MAIN SECTIONS ---
# 1. FEED THE LIBRARIAN
st.header("1. Feed the Librarian")
user_input = st.text_area("Log a new project:", height=100)
if st.button("Analyze & Save"):
    if user_input:
        with st.spinner("Extracting skills..."):
            bridge_process(user_input)
            st.success("Saved to Ledger!")

st.markdown("---")

# 2. THE VAULT
st.header("2. Your Skill Vault")
if all_data['ids']:
    # Simple text list for compatibility
    st.write(f"**Current Skills:** {', '.join(all_data['documents'])}")
else:
    st.write("Vault is empty.")

st.markdown("---")

# --- NEW SECTION: THE CAREER CHATBOT ---
st.header("3. Chat with your Career Advisor")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    if role == "user":
        st.info(f"👤 YOU: {content}")
    else:
        st.success(f"🤖 SCA AGENT: {content}")

# The Chat Input
question = st.text_input("Ask a question about your career data:", key="chat_input")

if st.button("Ask Agent"):
    if question:
        # 1. Add user message to history
        st.session_state.messages.append({"role": "user", "content": question})
        
        # 2. Retrieve relevant context from ChromaDB
        results = collection.query(query_texts=[question], n_results=5)
        context = ", ".join(results['documents'][0])
        
        # 3. Construct the RAG Prompt
        rag_prompt = f"""
        You are a Career Advisor. Answer the question based ONLY on the user's skills below.
        
        USER SKILLS: {context}
        
        USER QUESTION: {question}
        
        Keep the answer short, encouraging, and strategic.
        """
        
        # 4. Get Answer from Ollama
        with st.spinner("Thinking..."):
            response = ollama.generate(model='phi3', prompt=rag_prompt)
            answer = response['response']
        
        # 5. Add AI response to history
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
        # 6. Rerun to show new message
        try:
            st.rerun()
        except AttributeError:
            st.experimental_rerun()