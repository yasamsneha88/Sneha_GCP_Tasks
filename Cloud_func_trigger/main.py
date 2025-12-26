import functions_framework

@functions_framework.cloud_event
def on_file_upload(cloud_event):
    data = cloud_event.data or {}

    print("CLOUD STORAGE EVENT RECEIVED")
    print("Bucket:", data.get("bucket"))
    print("File:", data.get("name"))
    print("Size:", data.get("size"))
    print("Content Type:", data.get("contentType"))