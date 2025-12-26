import base64
import json
import os
from datetime import datetime
import mysql.connector

# ---------- Cloud SQL Connection ----------
def get_connection():
    return mysql.connector.connect(
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        database=os.environ["DB_NAME"],
        unix_socket=os.environ["DB_SOCKET"]
    )

# ---------- Pub/Sub HTTP Handler ----------
def pubsub_trigger(request):
    try:
        envelope = request.get_json(silent=True)

        if not envelope or "message" not in envelope:
            print("Invalid Pub/Sub message")
            return ("Bad Request", 400)

        # Decode Pub/Sub message
        pubsub_message = envelope["message"]
        data = base64.b64decode(pubsub_message["data"]).decode("utf-8")
        payload = json.loads(data)

        user_name = payload["user"]
        event_name = payload["event"]

        print("Event received:", payload)

        # Database connection
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        # Fetch user
        cursor.execute(
            "SELECT * FROM users WHERE name = %s LIMIT 1",
            (user_name,)
        )
        user = cursor.fetchone()

        if not user:
            print("User not found")
            cursor.close()
            conn.close()
            return ("OK", 200)

        # ---------- Business Logic ----------
        score = user["logins"] * 10

        if user["is_active"]:
            score += 50

        if user["age"] < 25:
            score += 20

        # Store score
        cursor.execute(
            """
            INSERT INTO user_scores (user_id, event_name, score, calculated_at)
            VALUES (%s, %s, %s, %s)
            """,
            (user["id"], event_name, score, datetime.utcnow())
        )

        conn.commit()
        cursor.close()
        conn.close()

        print("Score calculated and stored:", score)
        return ("OK", 200)

    except Exception as e:
        print("ERROR:", str(e))
        return ("Internal Server Error", 500)