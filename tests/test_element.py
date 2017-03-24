import unittest
from refract import Element


class ElementTests(unittest.TestCase):
    def test_element(self):
        element = Element('string', content='Hello World')
        self.assertEqual(element.element, 'string')
        self.assertEqual(element.content, 'Hello World')
