from bucket import Bucket
from utils.bucket_reader import read, get_bucket


def my_method(bucket_name: str, blob_name: str) -> str:
    bucket_to_read = get_bucket(bucket_name)
    return read(bucket_to_read, blob_name)


def my_other_method(bucket: Bucket) -> tuple:
    bucket_name_prefix = bucket.get_prefix()
    bucket_name_1 = bucket_name_prefix + "_name_1"
    b1 = get_bucket(bucket_name_1)
    bucket_name_2 = bucket_name_prefix + "_name_2"
    b2 = get_bucket(bucket_name_2)
    return b1, b2
