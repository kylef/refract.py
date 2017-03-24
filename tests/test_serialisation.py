import unittest
from refract import Element, MemberContent


class SerialisationTests(unittest.TestCase):
    def test_serialise_string(self):
        element = Element('string', content='Hello World')
        self.assertEqual(element.as_dict(), {
            'element': 'string',
            'content': 'Hello World',
        })

    def test_serialise_number(self):
        element = Element('number', content=3)
        self.assertEqual(element.as_dict(), {
            'element': 'number',
            'content': 3,
        })

    def test_serialise_boolean(self):
        element = Element('boolean', content=True)
        self.assertEqual(element.as_dict(), {
            'element': 'boolean',
            'content': True,
        })

    def test_serialise_null(self):
        element = Element('null', content=None)
        self.assertEqual(element.as_dict(), {
            'element': 'null',
            'content': None,
        })

    def test_serialise_object(self):
        element = Element('object', content=[
            Element('member', content=MemberContent(
                key=Element('string', content='id'),
                value=Element('string', content='Hello World')
            ))
        ])
        self.assertEqual(element.as_dict(), {
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
            Element('string', 'Hello World')
        ])

        self.assertEqual(element.as_dict(), {
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
        self.assertEqual(element.as_dict(), {
            'element': 'custom',
            'content': {
                'element': 'string',
                'content': 'Hello'
            }
        })
