import unittest
from refract import Array, String


class ArrayTests(unittest.TestCase):
    def setUp(self):
        self.title = String(content='title')
        self.hello = String(content='hello')
        self.array = Array(content=[self.title, self.hello])

    def test_initialisation(self):
        self.assertEqual(self.array.content, [self.title, self.hello])

    def test_len(self):
        self.assertEqual(len(self.array), 2)

    def test_subscript(self):
        self.assertEqual(self.array[0], self.title)
        self.assertEqual(self.array[1], self.hello)
