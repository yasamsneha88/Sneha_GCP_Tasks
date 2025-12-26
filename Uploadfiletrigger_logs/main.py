import logging
import functions_framework

@functions_framework.cloud_event
def uploadfile_triggerlogs(cloud_event):
    data = cloud_event.data or {}
    logging.info(f"File uploaded: {data.get('name')}")
    logging.info(f"Bucket: {data.get('bucket')}")