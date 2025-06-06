import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_chat(messages: list, model="gpt-4o") -> str:
    """
    Send a chat prompt to OpenAI and return the response.
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content