import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import openai as oai


# Initialize 
# api_key = "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"  
client = oai.OpenAI(api_key="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")


def chatbot():
    print("it is working")
    
    while True:
        user_input = input("chatbot input: ")
        
        if user_input.lower() == "":
            print("You are ending the bot.")
            break

        try:
            response = oai.chat.completions.create(
                model="gpt-4", 
                messages=[
                    # {"role": "system", "content": "CatBOT here: "},
                    {"role": "user", "content": user_input}
                ])
            # Changto "gpt-4" if you prefer
            # print(response)  # response structure

            if response.choices and len(response.choices) > 0:
                reply = response.choices[0].message.content
                print("CatBOT:", reply)
            else:
                print("CatBOT: (No response received)")

        except Exception as e:
            print("Error:", e)


# if __name__ == "__main_lucy__":
chatbot()