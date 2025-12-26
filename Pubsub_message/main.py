import functions_framework
import base64
import json
from google.cloud import bigquery
from datetime import datetime

bq_client = bigquery.Client()

@functions_framework.cloud_event
def pubsub_to_bigquery(cloud_event):
    msg = cloud_event.data["message"]
    payload = base64.b64decode(msg["data"]).decode("utf-8")
    data = json.loads(payload)

    row = {
        "event": data.get("event"),
        "user": data.get("user"),
        "ts": datetime.utcnow().isoformat()
    }

    # FORMAT: PROJECT_ID.DATASET_ID.TABLE_NAME
    table_id = "YOUR_PROJECT_ID.YOUR_DATASET_ID.YOUR_TABLE_NAME"

    errors = bq_client.insert_rows_json(table_id, [row])

    if errors:
        print(f"BigQuery Insert Failed: {errors}")
        raise RuntimeError(errors)

    print("BigQuery Insert Successful", row)