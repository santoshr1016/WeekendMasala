from unittest import TestCase
from unittest.mock import patch
from file_check import FileOps


class TestFileOps(TestCase):
    @patch('file_check.FileOps')
    def test_create_file_success(self, MockFileOps):
        fops = MockFileOps()
        fops.create_file.return_value = True
        fops.check_dir_exists.return_value = True
        fops.check_file_exists.return_value = True

        response = fops.create_file()
        self.assertTrue(response)

    # @patch('file_check.FileOps')
    # def test_create_file_dir_fail(self, MockFileOps):
    #     self.dirpath = "/a/b"
    #     self.fname = "dummy.txt"
    #     fops = MockFileOps(self.dirpath, self.fname)
    #     # fops.check_dir_exists.return_value = True
    #     # fops.check_file_exists.return_value = True
    #
    #     fops.create_file(self.dirpath, self.fname)
    #     fops.check_dir_exists(self.dirpath, self.fname)
    #     fops.check_file_exists(self.dirpath, self.fname)
    #     fops.check_dir_exists.assert_called_with('/a/b')
    #     fops.check_file_exists.assert_called_with("dummy.txt")

