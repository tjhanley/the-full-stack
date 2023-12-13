from fastapi import FastAPI
from dotenv import load_dotenv
from openai import OpenAI
from the_full_stack.models.gpt_request import GPTRequest

load_dotenv()  # take environment variables from .env.

app = FastAPI()
client = OpenAI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/gpt")
def post_gpt(request: GPTRequest):
    try:
        completion = client.chat.completions.create(
            model=request.gpt_model,
            messages=[
                {"role": msg.role, "content": msg.content} for msg in request.messages
            ],
        )
        return completion.choices[0].message
    except Exception as e:
        return {"error": str(e)}
