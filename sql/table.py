import sqlite3

conn = sqlite3.connect("GameBot.db")
cursor = conn.cursor()


def create_table():
    try:
        cursor.execute(
            "create table if not exists users (id INTEGER primary key AUTOINCREMENT, full_name TEXT, phone_number TEXT, chat_id INTEGER, created_at TEXT)")
        conn.commit()
    except Exception as exc:
        print(exc)
