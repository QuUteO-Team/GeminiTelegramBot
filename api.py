from fastapi import FastAPI
from gemini_client import ai_generate

app = FastAPI()

@app.post("/request")
def send_prompt(
        prompt: str
):
    answer = ai_generate(prompt)

    return {"answer": answer}

