from unittest import TestCase
from unittest.mock import patch, MagicMock
from my_module import my_method


class MyTest(TestCase):

    @patch('my_module.read')
    @patch('my_module.get_bucket')
    def test_my_method(self, mock_get_bucket, mock_read):
        blob_name = "test_blob.csv"
        bucket_name = 'my_bucket_name'
        mock_bucket = MagicMock()
        mock_get_bucket.return_value = mock_bucket
        expected = "mock blob content"
        mock_read.return_value = expected

        result = my_method(bucket_name, blob_name)

        mock_get_bucket.assert_called_once_with(bucket_name)
        mock_read.assert_called_once_with(mock_bucket, blob_name)
        self.assertEqual(expected, result)
