from utils.bucket_reader import read, get_bucket


def my_method(bucket_name, blob_name):
  bucket_to_read = get_bucket(bucket_name)
  return read(bucket_to_read, blob_name)