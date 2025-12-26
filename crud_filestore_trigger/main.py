import functions_framework
import json

@functions_framework.cloud_event
def on_user_create(cloud_event):
    data = cloud_event.data or {}
    value = data.get("value", {})
    fields = value.get("fields", {})

    def get_string(field):
        return fields.get(field, {}).get("stringValue")

    def get_int(field):
        val = fields.get(field, {}).get("integerValue")
        return int(val) if val else None

    print("FIRESTORE CREATE EVENT")
    print(json.dumps({
        "name": get_string("name"),
        "email": get_string("email"),
        "role": get_string("role"),
        "exp": get_int("exp")
    }, indent=2))