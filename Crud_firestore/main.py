from google.cloud import firestore

db = firestore.Client()

def create_user(request):
    data = request.get_json()
    db.collection("users").add(data)
    return "User Created"

def get_users(request):
    users = [doc.to_dict() for doc in db.collection("users").stream()]
    return {"users": users}

def update_user(request):
    data = request.get_json()
    db.collection("users").document(data["id"]).update(data)
    return "User Updated"

def delete_user(request):
    uid = request.args.get("id")
    db.collection("users").document(uid).delete()
    return "User Deleted"