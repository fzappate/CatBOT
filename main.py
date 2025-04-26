import streamlit as st
import openai as oai


# Set your API key
oai.api_key = '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'


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
