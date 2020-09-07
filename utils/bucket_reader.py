from google.cloud import storage
from bucket import Bucket


def get_bucket(bucket_name: str) -> Bucket:
    # instantiating object Bucket here
    return Bucket("some bucket")


def read(bucket_to_read: Bucket, blob_name: str) -> str:
    # reading content of some file stored in a GCP bucket and returning in a form of string
    blob = storage.Blob(blob_name)
    result = blob.download_as_string(client=bucket_to_read.client)
    return result
