import httpx

class Gemini_Service:
    def __init__(self, BACKEND_URL: str):
        self.BACKEND_URL = BACKEND_URL

    async def send_prompt(self, prompt: str) -> str:
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                response = await client.post(
                    self.BACKEND_URL,
                    json={"prompt": prompt},
                )
                response.raise_for_status()

                data = response.json()
                return data.get("answer", "Бэкенд прислал пустой ответ")
            except Exception as e:
                return f"❌ Ошибка связи с бэкендом: {e}"