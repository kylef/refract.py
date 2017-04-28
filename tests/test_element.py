import unittest
from refract import Element, String


class ElementTests(unittest.TestCase):
    def test_element(self):
        element = Element('string', content='Hello World')
        self.assertEqual(element.element, 'string')
        self.assertEqual(element.content, 'Hello World')

    def test_repr(self):
        element = Element('string', content='Hello World')
        self.assertEqual(repr(element), "<Element(string) content='Hello World'>")

        element = Element('array', content=[String('Hello World')])
        self.assertEqual(repr(element), "<Element(array) content=[<Element(string) content=None>]>")
