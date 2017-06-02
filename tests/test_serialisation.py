import unittest
from refract.json import JSONSerialiser, CompactJSONSerialiser
from refract import (Element, String, Number, Boolean, Null, Array, Metadata,
                     KeyValuePair)


class JSONSerialisationTests(unittest.TestCase):
    def setUp(self):
        self.serialiser = JSONSerialiser()

    def serialise(self, element):
        return self.serialiser.serialise_dict(element)

    def test_serialise_element_as_json(self):
        element = Element('string')
        serialised = self.serialiser.serialise(element)
        self.assertEqual(serialised, '{"element": "string"}')

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

    def test_serialise_object_empty_value(self):
        element = Element('object', content=[
            Element('member', content=KeyValuePair(
                key=Element('string', content='id'),
                value=Array()
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
                            'element': 'array',
                            'content': [],
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
        meta = Metadata(title=String(content='Test'))
        element = Element('string', meta=meta)

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
        meta = Metadata(description=String(content='Test'))
        element = Element('string', meta=meta)

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
        element = Element('string', meta=Metadata(classes=Array(content=[
            String(content='warning')
        ])))

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

    def test_serialise_empty_meta(self):
        element = Element('string', meta=Metadata(classes=Array(content=[])))

        self.assertEqual(self.serialise(element), {
            'element': 'string',
            'meta': {
                'classes': {
                    'element': 'array',
                    'content': []
                }
            }
        })

    def test_serialise_meta_links(self):
        element = Element('string', meta=Metadata(links=Array(content=[
            Element('link', content='https://example.com')
        ])))

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
        pointer = Element('ref', content='Test')
        element = Element('string', meta=Metadata(ref=pointer))

        self.assertEqual(self.serialise(element), {
            'element': 'string',
            'meta': {
                'ref': {
                    'element': 'ref',
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


class CompactJSONSerialisationTests(unittest.TestCase):
    def setUp(self):
        self.serialiser = CompactJSONSerialiser()

    def test_serialise_string_element(self):
        payload = self.serialiser.serialise(String(content='Hello'))
        self.assertEqual(payload, '["string", null, null, "Hello"]')

    def test_serialise_number_element(self):
        payload = self.serialiser.serialise(Number(content=2))
        self.assertEqual(payload, '["number", null, null, 2]')

    def test_serialise_boolean_element(self):
        payload = self.serialiser.serialise(Boolean(content=True))
        self.assertEqual(payload, '["boolean", null, null, true]')

    def test_serialise_null_element(self):
        payload = self.serialiser.serialise(Null())
        self.assertEqual(payload, '["null", null, null, null]')

    def test_serialise_element_element(self):
        payload = self.serialiser.serialise(Element('test',
                                            content=String(content='value')))
        self.assertEqual(payload, '["test", null, null, '
                                  '["string", null, null, "value"]]')

    def test_serialise_array_element(self):
        payload = self.serialiser.serialise(Element('array',
                                            content=[String(content='value')]))
        self.assertEqual(payload, '["array", null, null, '
                                  '[["string", null, null, "value"]]]')

    def test_serialise_key_value_pair_element(self):
        pair = KeyValuePair(
            key=String(content='name'),
            value=String(content='Doe')
        )
        payload = self.serialiser.serialise(Element('member', content=pair))

        self.assertEqual(payload, '["member", null, null, ["pair", '
                                  '["string", null, null, "name"], '
                                  '["string", null, null, "Doe"]'
                                  ']]')

    def test_serialise_meta(self):
        element = String(content='Hello')
        element.title = 'Title'
        payload = self.serialiser.serialise(element)
        self.assertEqual(payload, '["string", {"title": ["string", null, '
                                  'null, "Title"]}, null, "Hello"]')

    def test_serialise_attributes(self):
        element = String(content='Hello')
        element.attributes = {'contentType': String(content='text')}
        payload = self.serialiser.serialise(element)
        self.assertEqual(payload, '["string", null, {"contentType": '
                                  '["string", null, null, "text"]}, "Hello"]')
