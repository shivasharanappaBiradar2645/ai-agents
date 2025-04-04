from api import GeminiApi
from dotenv import load_dotenv
import os

load_dotenv()

api = GeminiApi(os.getenv('GEMINI_API_KEY'))

while True:
    ass = input(">> ")
    print(api.ask(query=ass))