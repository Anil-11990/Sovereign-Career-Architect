import ollama

# This is the "System Prompt" - it tells the AI who it is.
# We are defining its persona here.
SYSTEM_PROMPT = """
You are the 'Librarian', a specialized AI agent for the Sovereign Career Architect (SCA).
Your goal is to analyze raw text and extract structured 'Skills'.
Do not be chatty. Output only the requested data.
"""

def test_local_brain():
    print("--- [SCA SYSTEM START] ---")
    print("Connecting to local Llama 3 model...")

    # The user input (This is just a test to see if it works)
    user_input = "I built a Flask app that uses a tailored K-Means algorithm for clustering data."

    # This is the API call to your LOCAL machine, not the internet.
    response = ollama.chat(model='phi3', messages=[
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': f"Extract the technical skills from this sentence: '{user_input}'"}
    ])

    # The 'content' field holds the AI's reply
    print("\n[LIBRARIAN ANALYSIS]:")
    print(response['message']['content'])
    print("\n--- [SCA SYSTEM END] ---")

if __name__ == "__main__":
    test_local_brain()