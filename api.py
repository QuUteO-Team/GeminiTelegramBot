from fastapi import FastAPI
from pydantic import BaseModel
from gemini_client import ai_generate  # Это имя остается, но внутри теперь Groq
from database import db
import uvicorn

app = FastAPI()

class PromptRequest(BaseModel):
    user_id: int
    prompt: str

@app.on_event("startup")
async def startup():
    await db.setup()

@app.post("/request")
async def send_prompt(request: PromptRequest):
    # 1. Получаем ответ от Groq
    answer = ai_generate.generate(request.prompt)

    # 2. Логируем запрос и ответ в базу данных
    try:
        await db.log_request(request.user_id, request.prompt, answer)
    except Exception as e:
        print(f"Ошибка записи в БД: {e}")

    return {"answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)