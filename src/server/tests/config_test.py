import unittest
from src.config import resolve_path, parse, ingest


class TestConfigParser(unittest.TestCase):
    def setUp(self):
        """
        Setup stub data to represent config

        :return:
        """
        self.config_stub = {
            'general': {
                'app_name': 'app_name',
                'environment': 'test',
                'log_path': '/var/www/log/itn_test.log'
            },
            'db': {
                'host': 'localhost',
                'database': 'example',
                'user': 'example-user',
                'password': 'password',
                'port': 6379
            }
        }

    def test_resolve_path(self):
        """
        Assert the resolve path has conf in path

        :return:
        """
        self.assertIn('conf', resolve_path())

    def test_ingest(self):
        """
        Assert ingest returns a tuple

        :return:
        """
        self.assertIsInstance(ingest(self.config_stub), tuple)


if __name__ == '__main__':
    unittest.main()
