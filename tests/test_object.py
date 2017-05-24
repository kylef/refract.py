import unittest
from refract import Object, Member, String


class ObjectTests(unittest.TestCase):
    def setUp(self):
        self.key = String(content='title')
        self.value = String(content='hello')
        self.member = Member(key=self.key, value=self.value)
        self.object = Object(content=[self.member])

    def test_initialisation(self):
        self.assertEqual(self.object.content, [self.member])

    def test_initialisation_with_dict(self):
        obj = Object(content={'title': 'hello'})
        self.assertEqual(len(obj), 1)
        self.assertIsInstance(obj.children[0], Member)
        self.assertIsInstance(obj.children[0].key, String)
        self.assertIsInstance(obj.children[0].value, String)

    def test_len(self):
        self.assertEqual(len(self.object), 1)

    def test_getitem(self):
        value = self.object[self.key]
        self.assertEqual(value, self.value)

    def test_getitem_nonrefracted(self):
        value = self.object['title']
        self.assertEqual(value, self.value)

    def test_del(self):
        del self.object[self.key]
        self.assertEqual(len(self.object), 0)

    def test_del_nonrefracted(self):
        del self.object['title']
        self.assertEqual(len(self.object), 0)

    def test_del_clears_member_parent(self):
        del self.object[self.key]
        self.assertEqual(len(self.object), 0)
        self.assertIsNone(self.member.parent)

    def test_contains(self):
        self.assertTrue(self.key in self.object)
        self.assertTrue(self.value not in self.object)

    def test_contains_nonrefracted(self):
        self.assertTrue('title' in self.object)
        self.assertTrue('not title' not in self.object)

    def test_keys(self):
        self.assertEqual(self.object.keys(), [self.key])

    def test_values(self):
        self.assertEqual(self.object.values(), [self.value])
