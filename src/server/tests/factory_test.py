import unittest
from src.factory import generate_people, generate_person


class TestFactory(unittest.TestCase):
    def setUp(self):
        """
        Setup stub data to represent config

        :return:
        """
        self.res_stub = [{
            "id": 5,
            "name": "Alex Morgan",
            "img_url": "www.alexmorgan.com",
            "location": "California",
            "colors": ["Red", "Purple", "Orange"]
        }]

        self.stub = [(
            5,
            bytearray("Alex Morgan", 'utf-8'),
            bytearray("www.alexmorgan.com", 'utf-8'),
            bytearray("California", 'utf-8'),
            bytearray("Red,Purple,Orange", 'utf-8')
        )]

    def test_generate_person(self):
        """
        Assert factory method returns a dictionary

        :return:
        """
        self.assertEqual(self.res_stub[0], generate_person(self.stub[0]))

    def test_generate_people(self):
        """
        Assert factory method returns list of dictionary

        :return:
        """
        self.assertEqual(generate_people(self.stub), self.res_stub)


if __name__ == '__main__':
    unittest.main()
