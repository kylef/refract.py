import unittest
from refract import Element, String, Member, KeyValuePair


class ElementTests(unittest.TestCase):
    def test_element(self):
        element = Element('string', content='Hello World')
        self.assertEqual(element.element, 'string')
        self.assertEqual(element.content, 'Hello World')

    def test_repr(self):
        element = Element('string', content='Hello World')
        self.assertEqual(repr(element),
                         "<Element(string) content='Hello World'>")

        element = Element('array', content=[String('Hello World')])

        desc = "<Element(array) content=[<Element(string) content=None>]>"
        self.assertEqual(repr(element), desc)

    def test_no_value(self):
        element = Element('string')
        self.assertEqual(element.underlying_value, None)

    def test_string_value(self):
        element = Element('string', content='Hello World')
        self.assertEqual(element.underlying_value, 'Hello World')

    def test_number_value(self):
        element = Element('number', content=5)
        self.assertEqual(element.underlying_value, 5)

    def test_boolean_value(self):
        element = Element('boolean', content=True)
        self.assertEqual(element.underlying_value, True)

    def test_array_value(self):
        element = Element('array', content=[
            Element('String', content='Hello World')
        ])

        self.assertEqual(element.underlying_value, ['Hello World'])

    def test_key_value_pair_value(self):
        element = Element('element', content=KeyValuePair(
            key=String(content='key'),
            value=String(content='value')
        ))

        self.assertEqual(element.underlying_value, ('key', 'value'))

    def test_object_value(self):
        element = Element('object', content=[
            Member(key=String(content='key'), value=String(content='value'))
        ])
        self.assertEqual(element.underlying_value, {'key': 'value'})

    # Children

    def test_children_string(self):
        element = Element('string', content='hello world')
        self.assertEqual(element.children, [])

    def test_children_array(self):
        element = Element('things', content=[
            Element('string', content='hello world')
        ])
        self.assertEqual(len(element.children), 1)

    def test_children_direct_element(self):
        element = Element('thing',
                          content=Element('string', content='hello world'))

        self.assertEqual(len(element.children), 1)

    # Recursive Children

    def test_recursive_children_string(self):
        element = Element('string', content='hello world')
        self.assertEqual(len(list(element.recursive_children)), 0)

    def test_children_array(self):
        element = Element('things', content=[
            Element('morethings', content=[
                Element('string', content='hi')
            ])
        ])

        self.assertEqual(len(list(element.recursive_children)), 2)

    def test_children_array_with_direct_element(self):
        element = Element('things', content=[
            Element('morethings', content=[
                Element('thing', content=Element('string', content='hi'))
            ])
        ])

        self.assertEqual(len(list(element.recursive_children)), 3)
