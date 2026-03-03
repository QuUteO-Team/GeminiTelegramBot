from gemini_client import ai_generate
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str

@app.post("/request")

def send_prompt(request: PromptRequest):
    answer = ai_generate.generate(request.prompt)

    return {"answer": answer}