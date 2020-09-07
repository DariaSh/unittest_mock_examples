from google.cloud.storage import Client


class Bucket:

    def __init__(self, working_project: str):
        self.prefix = ''
        self.storage_client = Client(project=working_project)

    def get_bucket(self, bucket_name: str):
        return self.storage_client.get_bucket(bucket_name)

    def set_prefix(self, prefix):
        self.prefix = prefix

    def get_prefix(self) -> str:
        return self.prefix