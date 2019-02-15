import unittest
from unittest import mock
from worker import Worker, Helper


class MyTestCase(unittest.TestCase):
    @mock.patch('worker.Helper')
    def test_patching_class(self, MockHelper):
        MockHelper.return_value.get_path.return_value = 'testing'
        w = Worker()
        MockHelper.assert_called_once_with('db')
        self.assertEqual(w.work(), 'testing')


if __name__ == '__main__':
    unittest.main()
