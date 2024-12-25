import psycopg2
from datetime import datetime
import json
from typing import Dict

class DAO:
    def __init__(self, dbname: str, user: str, password: str, host: str = 'localhost', port: str = '5432'):
        """
        Инициализация подключения к PostgreSQL
        """
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def create_table(self):
        """
        Создание таблицы, если она не существует
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS conversation_history (
                    id SERIAL PRIMARY KEY,
                    request TEXT NOT NULL,
                    response TEXT NOT NULL,
                    dt TIMESTAMP NOT NULL
                );
            """)
        self.conn.commit()

    def log_conversation(self, request: str, response: str):
        """
        Запись диалога в базу данных
        """
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO conversation_history (request, response, dt)
                VALUES (%s, %s, %s);
            """, (request, response, datetime.now()))
        self.conn.commit()

    def get_history(self) -> list:
        """
        Получение всей истории диалогов
        """
        with self.conn.cursor() as cur:
            cur.execute("SELECT request, response, dt FROM conversation_history ORDER BY dt;")
            rows = cur.fetchall()
            return [
                {
                    'request': row[0],
                    'response': row[1],
                    'dt': row[2].isoformat()
                }
                for row in rows
            ]

    def close(self):
        """
        Закрытие соединения с базой данных
        """
        self.conn.close()
