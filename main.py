from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv(override=True)

google_api_key = os.getenv('GOOGLE_API_KEY')

if google_api_key:
    print(f"google API Key exists")
else:
    print("google API Key not set")

def callGemini():
    request = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
    request += "Answer only with the question, no explanation."
    messages = [{"role": "user", "content": request}]
    gemini = OpenAI(api_key=google_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
    model_name = "gemini-2.0-flash"

    response = gemini.chat.completions.create(model=model_name, messages=messages)
    answer = response.choices[0].message.content
    print(answer)
    

if __name__ == "__main__":
    callGemini()
    


