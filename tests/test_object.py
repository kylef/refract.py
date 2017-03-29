import unittest
from refract import Object, Member, String


class ObjectTests(unittest.TestCase):
    def setUp(self):
        self.key = String('title')
        self.value = String('hello')
        self.member = Member(key=self.key, value=self.value)
        self.object = Object([self.member])

    def test_initialisation(self):
        self.assertEqual(self.object.content, [self.member])

    def test_len(self):
        self.assertEqual(len(self.object), 1)

    def test_keys(self):
        self.assertEqual(self.object.keys(), [self.key])

    def test_values(self):
        self.assertEqual(self.object.values(), [self.value])
