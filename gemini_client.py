import os
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
from config import config_obj


class GigaChatClient:
    def __init__(self, credentials: str, model: str = "GigaChat"):
        self.credentials = credentials
        self.model = model

        self.client = GigaChat(
            credentials=credentials,
            scope="GIGACHAT_API_PERS",  # Ключевая строчка для бесплатного доступа
            model=model,
            verify_ssl_certs=False,
            timeout=60.0
        )

    def generate(self, prompt: str) -> str:
        try:
            chat = Chat(
                messages=[
                    Messages(
                        role=MessagesRole.USER,
                        content=prompt
                    )
                ]
            )

            response = self.client.chat(chat)

            if response.choices and len(response.choices) > 0:
                return response.choices[0].message.content
            else:
                return "❌ Не удалось получить ответ от GigaChat"

        except Exception as e:
            return f"❌ Ошибка при обращении к GigaChat API: {e}"

    def __del__(self):
        if hasattr(self, 'client'):
            self.client.close()


ai_generate = GigaChatClient(config_obj.GIGACHAT_CREDENTIALS)