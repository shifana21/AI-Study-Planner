import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("GEMINI_API_KEY not found!")
    exit()

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.8-flash"


)

response = chat.send_message(
    message="Give me one short study tip for a college student."
)

print(response.text)