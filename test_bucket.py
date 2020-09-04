from unittest import TestCase
from unittest.mock import patch
from bucket import Bucket


class BucketTest(TestCase):

        @patch('bucket.Client')
        def test_construct(self, mock_gcp_client):
            working_project = 'test project'
            bucket = Bucket(working_project)
            mock_gcp_client.assert_called_once_with(project=working_project)
            self.assertEqual(mock_gcp_client(), bucket.storage_client)

        def test_construct_context(self):
            working_project = 'test project'
            with patch('bucket.Client') as mock_gcp_client:
                bucket = Bucket(working_project)
                mock_gcp_client.assert_called_once_with(project=working_project)
                self.assertEqual(mock_gcp_client(), bucket.storage_client)