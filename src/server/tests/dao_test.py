import unittest
from unittest.mock import patch, Mock, MagicMock, mock_open, create_autospec
from src.dao import findOneOrNone, findAll
from mysql.connector import MySQLConnection


class TestDao(unittest.TestCase):
    def setUp(self):
        """
        Setup stub data

        :return:
        """
        self.stub = [(
            5,
            bytearray("Alex Morgan", 'utf-8'),
            bytearray("www.alexmorgan.com", 'utf-8'),
            bytearray("California", 'utf-8'),
            bytearray("Red,Purple,Orange", 'utf-8')
        )]

        self.stub_parsed = [{
            "id": 5,
            "name": "Alex Morgan",
            "img_url": "www.alexmorgan.com",
            "location": "California",
            "colors": ["Red", "Purple", "Orange"]
        }]

        self.mock = create_autospec(MySQLConnection, True)

    def test_find_all(self):
        """
        Assert find_all returns patched return value

        :return:
        """
        with patch('MySQLConnection.cursor.fetchall', return_value=self.stub):
            results = findAll(self.mock)
            self.assertEqual(results, self.stub_parsed)

    def test_find_one_or_none(self):
        """
        Assert find_one_or_none returns patched return value

        :return:
        """
        with patch('MySQLConnection.cursor.fetchone', return_value=self.stub[0]):
            results = findAll(self.mock)
            self.assertEqual(results, self.stub_parsed[0])


if __name__ == '__main__':
    unittest.main()
