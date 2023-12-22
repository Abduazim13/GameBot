import sqlite3

conn = sqlite3.connect("GameBot.db")
cursor = conn.cursor()


def get_user(chat_id: int):
    try:
        return cursor.execute(f"select * from users where chat_id={chat_id}").fetchone()
    except Exception as exc:
        print(exc)
        return False
