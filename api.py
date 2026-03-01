from fastapi import FastAPI
from gemini_client import generate_content

app = FastAPI()

@app.post("/request")
def send_prompt(
        prompt: str
):
    answer = generate_content(prompt)

    return {"answer": answer}

