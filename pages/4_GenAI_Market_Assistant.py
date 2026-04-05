import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Real Estate Copilot", page_icon="🤖", layout="centered")
st.title("🤖 Gurgaon Market Assistant")
st.write("Ask about current property rates, news, or future developments in Gurgaon. I search the live web for answers!")

# Initialize the Gemini Client using Streamlit Secrets
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("API Key not found. Please create a '.streamlit/secrets.toml' file and add GEMINI_API_KEY='your_key_here'.")
    st.stop()

# Define strict System Instructions
SYSTEM_PROMPT = """
You are an expert Real Estate and Infrastructure AI Assistant specifically for Gurgaon, Haryana.
Strict Rules:
1. Scope: Only answer questions related to real estate, infrastructure, or the Gurgaon market. Refuse other topics politely.
2. Context: Always assume the user is asking about Gurgaon, Haryana unless specified otherwise.
3. Data: Prioritize live search data. Quote prices in Crores (Cr) or Lakhs (L).
4. Conciseness: Keep answers brief, direct, and to the point (maximum 3-4 short sentences or bullet points) to save tokens.
5. Sources: ALWAYS explicitly state the source of your information at the end of your response (e.g., 'Source: MagicBricks' or 'Source: Economic Times').
6. Honesty: If you cannot find recent data, admit it rather than guessing.
"""

# Initialize chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "model", "content": "Hi! I'm your live Gurgaon real estate assistant. What would you like to know?"}
    ]

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("E.g., What are the current property rates in Sector 102?"):
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call Gemini API with Google Search and System Instructions
    with st.chat_message("model"):
        with st.spinner("Searching the web..."):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        tools=[{"google_search": {}}],
                        temperature=0.2 # Low temperature for factual consistency
                    )
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "model", "content": response.text})
                
            except Exception as e:
                st.error(f"An error occurred: {e}")