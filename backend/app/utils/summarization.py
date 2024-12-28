import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")

def summarize_text(transcript):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant summarizing meeting transcripts."},
            {"role": "user", "content": transcript},
        ],
    )
    return response['choices'][0]['message']['content']
