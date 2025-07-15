import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Test message for GPT-4"}],
        max_tokens=50
    )
    print("GPT-4 Response:", response['choices'][0]['message']['content'])
except Exception as e:
    print("Error:", e)
