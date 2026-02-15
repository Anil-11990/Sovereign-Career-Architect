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
st.subheader("Your Local AI-Powered Career Strategist")

# --- SIDEBAR: STATISTICS ---
all_data = collection.get()
st.sidebar.header("Skill DNA Stats")
st.sidebar.write(f"Total Skills Logged: **{len(all_data['ids'])}**")

if st.sidebar.button("Refresh Data"):
    # Compatibility Fix for st.rerun()
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()

# --- SECTION 1: ADD NEW EXPERIENCE ---
st.header("1. Feed the Librarian")
user_input = st.text_area("What did you work on today?", placeholder="e.g., I built a React dashboard...")

if st.button("Analyze & Save"):
    if user_input:
        with st.spinner("Librarian is thinking..."):
            bridge_process(user_input)
            st.success("Skills extracted and saved to Ledger!")
    else:
        st.warning("Please enter some text first.")

# Compatibility Fix for st.divider()
st.markdown("---") 

# --- SECTION 2: THE VAULT ---
st.header("2. Your Skill Vault")
if all_data['ids']:
    cols = st.columns(3)
    for i, skill in enumerate(all_data['documents']):
        cols[i % 3].info(f"🔹 {skill}")
else:
    st.write("The vault is currently empty.")

st.markdown("---")

# --- SECTION 3: THE ARCHITECT'S VISION ---
st.header("3. Strategic Roadmap")
if st.button("Generate Final Report"):
    with st.spinner("Architect is calculating gaps..."):
        try:
            with open("Career_Roadmap.md", "r") as f:
                roadmap = f.read()
            st.markdown(roadmap)
        except FileNotFoundError:
            st.error("Roadmap not found. Run 'architect_v2.py' first!")