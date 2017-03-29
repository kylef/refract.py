import unittest
from refract import Member, String


class MemberTests(unittest.TestCase):
    def test_initialisation(self):
        key = String('title')
        value = String('hello')
        member = Member(key=key, value=value)

        self.assertEqual(member.content.key, key)
        self.assertEqual(member.content.value, value)

    def test_get_key(self):
        key = String('title')
        member = Member(key=key)

        self.assertEqual(member.key, key)

    def test_set_key(self):
        key = String('title')
        new_key = String('description')
        member = Member(key=key)
        member.key = new_key

        self.assertEqual(member.key, new_key)

    def test_get_value(self):
        key = String('title')
        value = String('hello')
        member = Member(key=key, value=value)

        self.assertEqual(member.value, value)

    def test_set_value(self):
        key = String('title')
        value = String('hello')
        new_value = String('hello world')
        member = Member(key=key, value=value)
        member.value = new_value

        self.assertEqual(member.value, new_value)
