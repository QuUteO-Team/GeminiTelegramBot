import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.BACKEND_URL = os.getenv("BACKEND_URL")
        self.GIGACHAT_CREDENTIALS = os.getenv("GIGACHAT_CREDENTIALS")  # Добавлена эта строка

config_obj = Config()