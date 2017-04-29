import unittest

from refract import (String, Number, Boolean, Null, Array, Object,
                     Member, refract)


class RefractTests(unittest.TestCase):
    def test_refracting_element(self):
        element = String(content='Hello')
        self.assertEqual(refract(element), element)

    def test_refracting_string(self):
        element = refract('Hello')
        self.assertIsInstance(element, String)
        self.assertEqual(element.content, 'Hello')

    def test_refracting_int(self):
        element = refract(1)
        self.assertIsInstance(element, Number)
        self.assertEqual(element.content, 1)

    def test_refracting_float(self):
        element = refract(1.0)
        self.assertIsInstance(element, Number)
        self.assertEqual(element.content, 1.0)

    def test_refracting_bool(self):
        element = refract(True)
        self.assertIsInstance(element, Boolean)
        self.assertEqual(element.content, True)

    def test_refracting_none(self):
        element = refract(None)
        self.assertIsInstance(element, Null)
        self.assertEqual(element.content, None)

    def test_refracting_list(self):
        element = refract([1, 2])
        self.assertIsInstance(element, Array)
        self.assertEqual(len(element), 2)
        self.assertIsInstance(element[0], Number)
        self.assertIsInstance(element[1], Number)
        self.assertEqual(element[0].content, 1)
        self.assertEqual(element[1].content, 2)

    def test_refracting_dict(self):
        element = refract({'name': 'Doe'})

        self.assertIsInstance(element, Object)
        self.assertEqual(len(element), 1)

        member = element.content[0]
        self.assertIsInstance(member, Member)
        self.assertIsInstance(member.key, String)
        self.assertEqual(member.key.content, 'name')
        self.assertIsInstance(member.value, String)
        self.assertEqual(member.value.content, 'Doe')

    def test_refracting_object(self):
        with self.assertRaises(ValueError):
            refract(object())
