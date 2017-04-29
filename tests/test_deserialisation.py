import unittest
from refract import Namespace, Element, String, Number, Boolean, Null, Array
from refract.json import JSONDeserialiser


class DeserialisationTests(unittest.TestCase):
    def setUp(self):
        self.deserialiser = JSONDeserialiser(Namespace())

    def deserialise(self, element_dict):
        return self.deserialiser.deserialise_dict(element_dict)

    def test_deserialise_json(self):
        element = self.deserialiser.deserialise('{"element": "string"}')
        self.assertIsInstance(element, String)
        self.assertEqual(element.element, 'string')

    def test_deserialise_string(self):
        element = self.deserialise({
            'element': 'string',
            'content': 'Hello World'
        })

        self.assertIsInstance(element, String)
        self.assertEqual(element.element, 'string')
        self.assertEqual(element.content, 'Hello World')

    def test_deserialise_number(self):
        element = self.deserialise({
            'element': 'number',
            'content': 3
        })

        self.assertIsInstance(element, Number)
        self.assertEqual(element.element, 'number')
        self.assertEqual(element.content, 3)

    def test_deserialise_boolean(self):
        element = self.deserialise({
            'element': 'boolean',
            'content': True
        })

        self.assertIsInstance(element, Boolean)
        self.assertEqual(element.element, 'boolean')
        self.assertEqual(element.content, True)

    def test_deserialise_null(self):
        element = self.deserialise({
            'element': 'null',
            'content': None
        })

        self.assertIsInstance(element, Null)
        self.assertEqual(element.element, 'null')
        self.assertEqual(element.content, None)

    def test_deserialise_object(self):
        element = self.deserialise({
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
        element = self.deserialise({
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
        element = self.deserialise({
            'element': 'custom',
            'content': {
                'element': 'string',
                'content': 'Hello'
            }
        })

        self.assertEqual(element.element, 'custom')
        self.assertIsInstance(element.content, Element)
        self.assertEqual(element.content.content, 'Hello')

    def test_deserialise_meta_id(self):
        element = self.deserialise({
            'element': 'string',
            'meta': {
                'id': {
                    'element': 'string',
                    'content': 'Hello'
                }
            }
        })

        self.assertIsInstance(element, Element)
        self.assertIsInstance(element.id, String)
        self.assertEqual(element.id.content, 'Hello')

    def test_deserialise_meta_title(self):
        element = self.deserialise({
            'element': 'string',
            'meta': {
                'title': {
                    'element': 'string',
                    'content': 'Hello'
                }
            }
        })

        self.assertIsInstance(element, Element)
        self.assertIsInstance(element.title, String)
        self.assertEqual(element.title.content, 'Hello')

    def test_deserialise_meta_description(self):
        element = self.deserialise({
            'element': 'string',
            'meta': {
                'description': {
                    'element': 'string',
                    'content': 'Hello'
                }
            }
        })

        self.assertIsInstance(element, Element)
        self.assertIsInstance(element.description, String)
        self.assertEqual(element.description.content, 'Hello')

    def test_deserialise_meta_links(self):
        element = self.deserialise({
            'element': 'string',
            'meta': {
                'links': {
                    'element': 'array',
                    'content': []
                }
            }
        })

        self.assertIsInstance(element, Element)
        self.assertIsInstance(element.links, Array)

    def test_deserialise_meta_classes(self):
        element = self.deserialise({
            'element': 'string',
            'meta': {
                'classes': {
                    'element': 'array',
                    'content': [
                        {
                            'element': 'string',
                            'content': 'warning',
                        }
                    ]
                }
            }
        })

        self.assertIsInstance(element, Element)
        self.assertIsInstance(element.classes, Array)
        self.assertIsInstance(element.classes.content[0], String)

    def test_deserialise_meta_ref(self):
        element = self.deserialise({
            'element': 'string',
            'meta': {
                'ref': {
                    'element': 'elementPointer',
                    'content': 'Test'
                }
            }
        })

        self.assertIsInstance(element, Element)
        self.assertIsInstance(element.ref, Element)
        self.assertEqual(element.ref.element, 'elementPointer')
        self.assertEqual(element.ref.content, 'Test')

    def test_deserialise_attributes(self):
        element = self.deserialise({
            'element': 'string',
            'attributes': {
                'test': {
                    'element': 'string',
                    'content': 'Hello'
                }
            }
        })

        self.assertIsInstance(element, Element)
        test_element = element.attributes['test']
        self.assertIsInstance(test_element, Element)
        self.assertEqual(test_element.element, 'string')
        self.assertEqual(test_element.content, 'Hello')
