users = {}

def create_user(request):
    data = request.get_json()
    users[data["id"]] = data
    return "User Created"

def read_user(request):
    uid = request.args.get("id")
    return users.get(uid, "User Not Found")

def update_user(request):
    data = request.get_json()
    users[data["id"]] = data
    return "User Updated"

def delete_user(request):
    uid = request.args.get("id")
    users.pop(uid, None)
    return "User Deleted"