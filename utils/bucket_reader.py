from google.cloud import storage
from bucket import Bucket


def get_bucket(project_name: str, bucket_name: str) -> Bucket:
    # instantiating object Bucket here
    return Bucket(project_name).get_bucket(bucket_name)


def read(bucket_to_read: Bucket, blob_name: str) -> str:
    # reading content of some file stored in a GCP bucket and returning in a form of string
    blob = storage.Blob(blob_name)
    result = blob.download_as_string(client=bucket_to_read.client)
    return result
