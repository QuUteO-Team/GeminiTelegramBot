import psycopg2
import asyncio
import os
from functools import partial

class Database:
    def __init__(self):
        self.conn_params = {
            "dbname": "geminiDB",
            "user": "user",
            "password": "user",
            "host": "localhost",
            "port": "5432"
        }


    async def _run_sync(self, func, *args):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, partial(func, *args))

    def _init_db_sync(self):
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                # Таблица подписок
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS subs (
                        chat_id BIGINT,
                        url TEXT,
                        last_match TIMESTAMP DEFAULT '1970-01-01',
                        UNIQUE(chat_id, url)
                    )
                """)
                # Таблица истории (Логирование)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS history (
                        id SERIAL PRIMARY KEY,
                        user_id BIGINT,
                        prompt TEXT,
                        response TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
            conn.commit()

    def _save_log_sync(self, user_id, prompt, response):
        with psycopg2.connect(**self.conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO history (user_id, prompt, response) VALUES (%s, %s, %s)",
                    (user_id, prompt, response)
                )
            conn.commit()

    async def setup(self):
        await self._run_sync(self._init_db_sync)

    async def log_request(self, user_id, prompt, response):
        await self._run_sync(self._save_log_sync, user_id, prompt, response)

db = Database()