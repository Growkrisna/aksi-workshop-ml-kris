from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
chat = client.chats.create(model="gemini-2.0-flash")

def chat_input(promp):
    respone = chat.send_message(promp)
    return respone.text

# input_text = input("Chat: ")
# chat_input(input_text)
# respone = chat_input(input_text)
    
# if __name__ == "__main__":
#     while True:
#         input_text = input("You: ")
#         if input_text.lower() in ["exit", "quit"]:
#             print("Exiting chat...")
#             break
#         response = chat.send_message(input_text)
#         print(f"AI: {response.text}")    
        
# def main():
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             print("Exiting chat...")
#             break
#         response = chat(user_input)
#         print(f"AI: {response}")