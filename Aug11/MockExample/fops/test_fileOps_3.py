from unittest import TestCase
from unittest.mock import patch
from file_check import FileOps


class TestFileOps(TestCase):
    @patch('file_check.FileOps')
    def test_create_file_dir_fail(self, MockFileOps):
        MockFileOps.return_value.create_file.return_value = True
        fops = FileOps("/a/b", "dummy.txt")
        MockFileOps.assert_called_with()
        # self.assertEqual(fops.create_file, True)
