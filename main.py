import streamlit as st
import openai as oai
from dotenv import load_dotenv
import os
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup

def read_epub(file_path):
    book = epub.read_epub(file_path)
    text = ""

    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text += soup.get_text()
    
    return text


def chat_with_openai(prompt):
    response = oai.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo" if you prefer
        messages=[
            {"role": "system", "content": "You are a very knoledgeable but faisty cat and you start every message with MEOW."},
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


load_dotenv()

# Set your API key
envvar = os.getenv('OPEN_API_KEY')
oai.api_key =  envvar

# Initialize the session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🐱📚 Chatbot - Powered by Streamlit + OpenAI")

# User input
user_input = st.text_input("You:", key="input")

epubContent = read_epub("Personal finance for dummies.epub")  # Replace with your EPUB file path


# Example loop
if __name__ == "__main__":
    
    # response = oai.chat.completions.create(
    # model="gpt-4",
    # messages=[
    #     {"role": "system", "content": "You are a helpful assistant that answers based only on the content of the uploaded EPUB."},
    #     {"role": "user", "content": f"Here is the EPUB content:\n{epubContent}\n\nRead this ebook and wait for questions?"}
    # ]
    # )
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        bot_response = chat_with_openai(user_input)
        print("Bot:", bot_response)
