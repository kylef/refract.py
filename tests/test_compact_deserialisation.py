import unittest
from refract import Element


class CompactDeserialisationTests(unittest.TestCase):
    def test_deserialise_string(self):
        element = Element.from_tuple(['string', [], [], 'Hello World'])

        self.assertEqual(element.element, 'string')
        self.assertEqual(element.content, 'Hello World')

    def test_deserialise_number(self):
        element = Element.from_tuple(['number', [], [], 3])

        self.assertEqual(element.element, 'number')
        self.assertEqual(element.content, 3)

    def test_deserialise_boolean(self):
        element = Element.from_tuple(['boolean', [], [], True])

        self.assertEqual(element.element, 'boolean')
        self.assertEqual(element.content, True)


    def test_deserialise_null(self):
        element = Element.from_tuple(['null', [], [], None])

        self.assertEqual(element.element, 'null')
        self.assertEqual(element.content, None)

    def test_deserialise_object(self):
        element = Element.from_tuple(['object', [], [], [
            ['member', [], [], [
                ['string', [], [], 'id'],
                ['string', [], [], 'Hello World'],
            ]]
        ]])

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
        element = Element.from_tuple(['array', [], [], [
            ['string', [], [], 'Hello World']
        ]])

        self.assertEqual(element.element, 'array')
        self.assertIsInstance(element.content, list)
        self.assertEqual(len(element.content), 1)
        self.assertIsInstance(element.content[0], Element)
        self.assertEqual(element.content[0].element, 'string')
        self.assertEqual(element.content[0].content, 'Hello World')

    def test_deserailise_custom(self):
        element = Element.from_tuple(['custom', [], [], [
            'string', [], [], 'Hello'
        ]])

        self.assertEqual(element.element, 'custom')
        self.assertIsInstance(element.content, Element)
        self.assertEqual(element.content.content, 'Hello')
