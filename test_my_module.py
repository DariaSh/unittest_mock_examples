from unittest import TestCase
from unittest.mock import patch, MagicMock, call
from my_module import my_method, my_other_method


class MyTest(TestCase):

    @patch('my_module.read')
    @patch('my_module.get_bucket')
    def test_my_method(self, mock_get_bucket, mock_read):
        blob_name = "test_blob.csv"
        project_name = 'my_project'
        bucket_name = 'my_bucket_name'
        mock_bucket = MagicMock()
        mock_get_bucket.return_value = mock_bucket
        expected = "mock blob content"
        mock_read.return_value = expected

        result = my_method(project_name, bucket_name, blob_name)

        mock_get_bucket.assert_called_once_with(project_name, bucket_name)
        mock_read.assert_called_once_with(mock_bucket, blob_name)
        self.assertEqual(expected, result)

    @patch('my_module.get_bucket')
    def test_my_other_method(self, mock_get_bucket):
        prefix = "my_bucket"
        mock_bucket = MagicMock()
        mock_bucket.get_prefix.return_value = prefix
        bucket_name_1 = "_name_1"
        bucket_name_2 = "_name_2"
        bucket_names = [prefix + bucket_name_1, prefix + bucket_name_2]
        my_other_method(mock_bucket)

        method_call_count = 2
        self.assertEqual(method_call_count, mock_get_bucket.call_count)
        for i in range(method_call_count):
            self.assertEqual(call(bucket_names[i]), mock_get_bucket.mock_calls[i])

    @patch('my_module.get_bucket')
    def test_my_other_method_as_list(self, mock_get_bucket):
        prefix = "my_bucket"
        mock_bucket = MagicMock()
        mock_bucket.get_prefix.return_value = prefix
        bucket_name_1 = "_name_1"
        bucket_name_2 = "_name_2"
        bucket_names = [prefix + bucket_name_1, prefix + bucket_name_2]
        expected_mock_calls = []

        for bucket_name in bucket_names:
            expected_mock_calls.append(call(bucket_name))

        my_other_method(mock_bucket)

        self.assertListEqual(expected_mock_calls, mock_get_bucket.mock_calls)
