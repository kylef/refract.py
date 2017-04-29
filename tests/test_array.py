import unittest
from refract import Array, String


class ArrayTests(unittest.TestCase):
    def setUp(self):
        self.title = String(content='title')
        self.hello = String(content='hello')
        self.array = Array(content=[self.title, self.hello])

    def test_initialisation(self):
        self.assertEqual(self.array.content, [self.title, self.hello])

    def test_initialisation_python_types(self):
        array = Array(content=['Hello'])
        self.assertIsInstance(array[0], String)
        self.assertEqual(array[0].content, 'Hello')

    def test_len(self):
        self.assertEqual(len(self.array), 2)

    def test_subscript(self):
        self.assertEqual(self.array[0], self.title)
        self.assertEqual(self.array[1], self.hello)

    def test_del(self):
        del self.array[0]
        self.assertEqual(len(self.array), 1)

    def test_contains(self):
        self.assertTrue(self.title in self.array)
        self.assertTrue(String(content='test') not in self.array)

    def test_contains_nonrefracted(self):
        self.assertTrue('title' in self.array)

    def test_append(self):
        self.array.append(String(content='final'))
        self.assertEqual(self.array[2].content, 'final')

    def test_append_nonrefracted(self):
        self.array.append('final')
        self.assertEqual(self.array[2].content, 'final')

    def test_insert(self):
        self.array.insert(0, String(content='final'))
        self.assertEqual(self.array[0].content, 'final')

    def test_insert_nonrefracted(self):
        self.array.insert(0, 'final')
        self.assertEqual(self.array[0].content, 'final')

    def test_index(self):
        index = self.array.index(self.array[1])
        self.assertEqual(index, 1)

    def test_clear(self):
        self.array.clear()
        self.assertEqual(len(self.array), 0)
