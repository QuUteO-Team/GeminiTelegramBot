import os

class Config:
    def __init__(self):
        self.GEMINI_API_KEY = os.getenv("API_KEY")

config_obj = Config()