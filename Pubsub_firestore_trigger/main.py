import functions_framework
import base64
import json
from datetime import datetime
from google.cloud import firestore

# Firestore client
db = firestore.Client()

@functions_framework.cloud_event
def pubsub_trigger(cloud_event):
    # Decode Pub/Sub message
    message = cloud_event.data["message"]
    data = base64.b64decode(message["data"]).decode("utf-8")
    payload = json.loads(data)

    user_name = payload.get("user")
    event_name = payload.get("event")

    print("Event received:", payload)

    # Fetch user from Firestore
    users_ref = db.collection("users")
    docs = users_ref.where("name", "==", user_name).limit(1).stream()

    user = None
    user_id = None
    for doc in docs:
        user = doc.to_dict()
        user_id = doc.id

    if not user:
        print("User not found")
        return

    print("User data:", user)

    # -------- Business Logic --------
    score = user.get("logins", 0) * 10

    if user.get("is_active"):
        score += 50

    if user.get("age", 0) < 25:
        score += 20

    # Store score in Firestore
    db.collection("user_scores").add({
        "user_name": user_name,
        "user_id": user_id,
        "event": event_name,
        "score": score,
        "calculated_at": datetime.utcnow()
    })

    print("Score calculated:", score)