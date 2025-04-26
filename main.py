import streamlit as st
import openai as oai
from dotenv import load_dotenv
import os
load_dotenv()

# Set your API key
oai.api_key =  os.getenv('OPEN_AI_API_KEY')


# Set your API keyhi

def chat_with_openai(prompt):
    response = oai.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if you prefer
        # messages=[
        #     {"role": "system", "content": "You are a helpful chatbot."},
        #     {"role": "user", "content": prompt}
        # ]
        messages=[
            {"role": "system", "content": "You are a very knoledgeable but faisty cat and you start every message with MEOW."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
    # return response['choices'][0]['message']['content']

# Example loop
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        bot_response = chat_with_openai(user_input)
        print("Bot:", bot_response)
