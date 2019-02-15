from unittest import TestCase
from unittest.mock import patch
from file_check import FileOps


class TestFileOps(TestCase):
    def setUp(self):
        self.dirpath = "/a/b"
        self.fname = "dummy.txt"
        self.fops = FileOps(self.dirpath, self.fname)

    @patch('file_check.FileOps.check_file_exists', return_value=True)
    @patch('file_check.FileOps.check_dir_exists', return_value=True)
    @patch('file_check.FileOps.create_file', return_value=False)
    def test_create_file_dir_fail(self, create_file, check_dir_exists, check_file_exists):
        self.assertEqual(create_file(), False)
        self.assertEqual(check_dir_exists(), True)
        self.assertEqual(check_file_exists(), True)


    @patch('file_check.FileOps.check_file_exists', return_value=True)
    @patch('file_check.FileOps.check_dir_exists', return_value=False)
    @patch('file_check.FileOps.create_file', return_value=True)
    def test_create_file_dir_fail_2(self, create_file, check_dir_exists, check_file_exists):
        self.fops.create_file()
        self.fops.check_dir_exists()
        self.fops.check_file_exists()
        assert create_file.called
        check_dir_exists.assert_called_with()
        check_file_exists.assert_called_once_with()
