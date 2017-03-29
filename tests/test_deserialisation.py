import unittest
from refract import Namespace, Element, String, Number, Boolean, Null


class DeserialisationTests(unittest.TestCase):
    def test_deserialise_string(self):
        element = Namespace().from_dict({
            'element': 'string',
            'content': 'Hello World'
        })

        self.assertIsInstance(element, String)
        self.assertEqual(element.element, 'string')
        self.assertEqual(element.content, 'Hello World')

    def test_deserialise_number(self):
        element = Namespace().from_dict({
            'element': 'number',
            'content': 3
        })

        self.assertIsInstance(element, Number)
        self.assertEqual(element.element, 'number')
        self.assertEqual(element.content, 3)

    def test_deserialise_boolean(self):
        element = Namespace().from_dict({
            'element': 'boolean',
            'content': True
        })

        self.assertIsInstance(element, Boolean)
        self.assertEqual(element.element, 'boolean')
        self.assertEqual(element.content, True)


    def test_deserialise_null(self):
        element = Namespace().from_dict({
            'element': 'null',
            'content': None
        })

        self.assertIsInstance(element, Null)
        self.assertEqual(element.element, 'null')
        self.assertEqual(element.content, None)

    def test_deserialise_object(self):
        element = Namespace().from_dict({
            'element': 'object',
            'content': [
                {
                    'element': 'member',
                    'content': {
                        'key': {
                            'element': 'string',
                            'content': 'id',
                        },
                        'value': {
                            'element': 'string',
                            'content': 'Hello World',
                        }
                    }
                }
            ]
        })

        self.assertEqual(element.element, 'object')
        self.assertIsInstance(element.content, list)
        self.assertEqual(len(element.content), 1)

        sub_element = element.content[0]
        self.assertIsInstance(sub_element, Element)

        self.assertEqual(sub_element.element, 'member')
        key = sub_element.content.key
        value = sub_element.content.value

        self.assertIsInstance(key, Element)
        self.assertEqual(key.element, 'string')
        self.assertEqual(key.content, 'id')

        self.assertIsInstance(value, Element)
        self.assertEqual(value.element, 'string')
        self.assertEqual(value.content, 'Hello World')

    def test_deserialise_array(self):
        element = Namespace().from_dict({
            'element': 'array',
            'content': [
                {
                    'element': 'string',
                    'content': 'Hello World',
                }
            ]
        })

        self.assertEqual(element.element, 'array')
        self.assertIsInstance(element.content, list)
        self.assertEqual(len(element.content), 1)
        self.assertIsInstance(element.content[0], Element)
        self.assertEqual(element.content[0].element, 'string')
        self.assertEqual(element.content[0].content, 'Hello World')

    def test_deserailise_custom(self):
        element = Namespace().from_dict({
            'element': 'custom',
            'content': {
                'element': 'string',
                'content': 'Hello'
            }
        })

        self.assertEqual(element.element, 'custom')
        self.assertIsInstance(element.content, Element)
        self.assertEqual(element.content.content, 'Hello')
