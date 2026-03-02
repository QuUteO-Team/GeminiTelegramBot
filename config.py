import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        self.BACKEND_URL = os.getenv("BACKEND_URL")

config_obj = Config()