import sqlite3

conn = sqlite3.connect("GameBot.db")
cursor = conn.cursor()


def insert_user(data: dict):
    try:
        full_name = data.get('full_name')
        phone_number = data.get('phone_number')
        created_at = data.get('created_at')
        chat_id = data.get('chat_id')
        cursor.execute(
            "INSERT INTO users (full_name, phone_number, chat_id, created_at) VALUES (?,?,?,?)",
            (full_name, phone_number, chat_id, created_at))
        conn.commit()
        return True
    except Exception as exc:
        print(exc)
        return False
