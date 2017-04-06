import unittest
from refract.json import JSONSerialiser
from refract import Element, String, Array, Metadata, KeyValuePair


class SerialisationTests(unittest.TestCase):
    def setUp(self):
        self.serialiser = JSONSerialiser()

    def serialise(self, element):
        return self.serialiser.serialise_dict(element)

    def test_serialise_string(self):
        element = Element('string', content='Hello World')
        self.assertEqual(self.serialise(element), {
            'element': 'string',
            'content': 'Hello World',
        })

    def test_serialise_number(self):
        element = Element('number', content=3)
        self.assertEqual(self.serialise(element), {
            'element': 'number',
            'content': 3,
        })

    def test_serialise_boolean(self):
        element = Element('boolean', content=True)
        self.assertEqual(self.serialise(element), {
            'element': 'boolean',
            'content': True,
        })

    def test_serialise_null(self):
        element = Element('null', content=None)
        self.assertEqual(self.serialise(element), {
            'element': 'null',
            'content': None,
        })

    def test_serialise_object(self):
        element = Element('object', content=[
            Element('member', content=KeyValuePair(
                key=Element('string', content='id'),
                value=Element('string', content='Hello World')
            ))
        ])
        self.assertEqual(self.serialise(element), {
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

    def test_serialise_array(self):
        element = Element('array', content=[
            Element('string', content='Hello World')
        ])

        self.assertEqual(self.serialise(element), {
            'element': 'array',
            'content': [
                {
                    'element': 'string',
                    'content': 'Hello World',
                }
            ]
        })

    def test_serailise_custom(self):
        element = Element('custom', content=Element('string', content='Hello'))
        self.assertEqual(self.serialise(element), {
            'element': 'custom',
            'content': {
                'element': 'string',
                'content': 'Hello'
            }
        })

    def test_serialise_meta_id(self):
        element = Element('string', meta=Metadata(id=String(content='Test')))
        self.assertEqual(self.serialise(element), {
            'element': 'string',
            'meta': {
                'id': {
                    'element': 'string',
                    'content': 'Test'
                }
            }
        })

    def test_serialise_meta_title(self):
        element = Element('string', meta=Metadata(title=String(content='Test')))
        self.assertEqual(self.serialise(element), {
            'element': 'string',
            'meta': {
                'title': {
                    'element': 'string',
                    'content': 'Test'
                }
            }
        })

    def test_serialise_meta_description(self):
        element = Element('string', meta=Metadata(description=String(content='Test')))
        self.assertEqual(self.serialise(element), {
            'element': 'string',
            'meta': {
                'description': {
                    'element': 'string',
                    'content': 'Test'
                }
            }
        })

    def test_serialise_meta_classes(self):
        element = Element('string', meta=Metadata(classes=Array(content=[String(content='warning')])))
        self.assertEqual(self.serialise(element), {
            'element': 'string',
            'meta': {
                'classes': {
                    'element': 'array',
                    'content': [
                        {
                            'element': 'string',
                            'content': 'warning'
                        }
                    ]
                }
            }
        })

    def test_serialise_meta_links(self):
        element = Element('string', meta=Metadata(links=Array(content=[Element('link', content='https://example.com')])))
        self.assertEqual(self.serialise(element), {
            'element': 'string',
            'meta': {
                'links': {
                    'element': 'array',
                    'content': [
                        {
                            'element': 'link',
                            'content': 'https://example.com'
                        }
                    ]
                }
            }
        })

    def test_serialise_meta_ref(self):
        element = Element('string', meta=Metadata(ref=Element('elementPointer', content='Test')))
        self.assertEqual(self.serialise(element), {
            'element': 'string',
            'meta': {
                'ref': {
                    'element': 'elementPointer',
                    'content': 'Test'
                }
            }
        })


    def test_serialise_attributes(self):
        element = Element('string', attributes={'test': Element('example')})
        self.assertEqual(self.serialise(element), {
            'element': 'string',
            'attributes': {
                'test': {
                    'element': 'example'
                }
            }
        })
