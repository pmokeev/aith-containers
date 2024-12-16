import os
import time
import psycopg2
from psycopg2 import Error

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("POSTGRES_HOST"),
                port=os.getenv("POSTGRES_PORT")
            )
            conn.close()
            return
        except Error:
            print("Waiting for database to be ready...")
            time.sleep(2)

def init_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT")
        )
        
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS hello_messages (
                id SERIAL PRIMARY KEY,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        cur.execute("""
            INSERT INTO hello_messages (message) 
            VALUES ('Hello Docker-Compose!')
            ON CONFLICT DO NOTHING;
        """)
        
        conn.commit()
        print("Database initialized successfully!")
        
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    wait_for_db()
    init_db()