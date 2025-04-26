import streamlit as st
import openai as oai
import os
from dotenv import load_dotenv

load_dotenv()

# oai.api_key = OPEN_AI_API_KEY
oai.api_key = os.getenv("OPEN_API_KEY")

print("API Key:", oai.api_key)  # Debugging line to check if the API key is loaded correctly

# Initialize the session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🐱📚 Chatbot - Powered by Streamlit + OpenAI")

# User input
user_input = st.text_input("You:", key="input")

# Chat with OpenAI
def chat_with_openai(prompt):
    response = oai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a wise, feisty cat. Start every answer with MEOW."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Handle user input
if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
    bot_response = chat_with_openai(user_input)

    # Add bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# Display conversation
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])
