import os
from dotenv import load_dotenv
from google import genai 
from models import PROMPT

load_dotenv()
client= genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def llm_initialize(prompt:PROMPT):
    response= client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt.prompt
    )
    return response.text