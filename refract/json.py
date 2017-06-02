import json

from refract.registry import Registry
from refract.elements import (Element, Attributes, Metadata, KeyValuePair,
                              String, Array)
from refract.refraction import refract


META_KEYS = ('id', 'title', 'description', 'classes', 'links', 'ref')


class JSONSerialiser:
    """
    JSON Refract Serialiser
    """

    def serialise_dict(self, element):
        element_dict = {
            'element': element.element,
        }

        meta = {}

        for key in META_KEYS:
            value = getattr(element.meta, key, None)
            if value is not None:
                meta[key] = self.serialise_dict(value)

        if meta:
            element_dict['meta'] = meta

        if element.attributes:
            element_dict['attributes'] = dict(
                [(k, self.serialise_dict(v))
                    for (k, v) in element.attributes.items()]
            )

        if element.content is not None or element.element == "null":
            if isinstance(element.content, KeyValuePair):
                content = {}

                if element.content.key is not None:
                    content['key'] = self.serialise_dict(element.content.key)

                if element.content.value is not None:
                    content['value'] = self.serialise_dict(
                        element.content.value
                    )

                element_dict['content'] = content
            elif isinstance(element.content, list):
                element_dict['content'] = \
                    [self.serialise_dict(e) for e in element.content]
            elif isinstance(element.content, Element):
                element_dict['content'] = self.serialise_dict(element.content)
            else:
                element_dict['content'] = element.content

        return element_dict

    def serialise(self, element: Element, **kwargs) -> str:
        """
        Serialises the given element into JSON.

        >>> JSONSerialiser().serialise(String(content='Hello'))
        '{"element": "string", "content": "Hello"}'
        """

        return json.dumps(self.serialise_dict(element), **kwargs)


class JSONDeserialiser:
    """
    JSON Refract Deserialiser
    """

    def __init__(self, registry: Registry=None) -> None:
        self.registry = registry or Registry()

    def deserialise_meta(self, element_dict):
        meta = Metadata()

        if 'meta' in element_dict:
            for key in META_KEYS:
                value = element_dict['meta'].get(key, None)
                if value:
                    setattr(meta, key, self.deserialise_dict(value))

        return meta

    def deserialise_attributes(self, element_dict):
        if 'attributes' in element_dict:
            return dict([(k, self.deserialise_dict(v))
                         for (k, v) in element_dict['attributes'].items()])

        return {}

    def deserialise_content(self, element_dict):
        if 'content' in element_dict:
            content = element_dict['content']

            if isinstance(content, list):
                return [self.deserialise_dict(e) for e in content]
            elif isinstance(content, dict):
                if 'element' in content:
                    return self.deserialise_dict(content)
                elif 'key' in content:
                    key = self.deserialise_dict(content['key'])

                    value = content.get('value')
                    if value:
                        value = self.deserialise_dict(value)

                    return KeyValuePair(key=key, value=value)
                else:
                    raise ValueError('Given element content contains object')
            else:
                return content

        return None

    def deserialise_dict(self, element_dict):
        if 'element' not in element_dict:
            raise ValueError(
                'Given element does not contain an element property'
            )

        cls = self.registry.find_element_class(element_dict['element'])
        element = cls()
        element.element = element_dict['element']
        element.content = self.deserialise_content(element_dict)
        element.meta = self.deserialise_meta(element_dict)
        element.attributes = self.deserialise_attributes(element_dict)
        return element

    def deserialise(self, element_json: str) -> Element:
        """
        Deserialises the given JSON into an element.

        >>> json = '{"element": "string", "content": "Hello"'
        >>> JSONDeserialiser().deserialise(json)
        String(content='Hello')
        """

        return self.deserialise_dict(json.loads(element_json))


class LegacyJSONDeserialiser(JSONDeserialiser):
    """
    Deserialiser for Refract 0.6.0 and below.
    """

    def deserialise_dict(self, element_dict):
        if isinstance(element_dict, (int, str, float)):
            return refract(element_dict)

        if isinstance(element_dict, list):
            return Array(content=[self.deserialise_dict(e)
                                  for e in element_dict])

        if isinstance(element_dict, dict) and 'key' not in element_dict \
                and 'element' not in element_dict:
            return Array(content=[self.deserialise_dict(e)
                                  for e in element_dict])

        return super(LegacyJSONDeserialiser, self).deserialise_dict(
            element_dict
        )

    def deserialise_content(self, element_dict):
        if 'content' in element_dict and \
                isinstance(element_dict['content'], dict):
            content = element_dict['content']

            if 'key' not in content and 'element' not in content and \
                    'href' in content:
                attributes = {}

                if 'path' in content:
                    attributes['path'] = String(content=content['path'])

                return Element(
                    'ref',
                    attributes=attributes,
                    content=content['href']
                )

        return super(LegacyJSONDeserialiser, self).deserialise_content(
            element_dict
        )


class CompactJSONSerialiser:
    def serialise_meta(self, meta: Metadata):
        metadata = {}

        for key in META_KEYS:
            value = getattr(meta, key, None)
            if value:
                metadata[key] = self.serialise_element(value)

        if metadata:
            return metadata

    def serialise_attributes(self, attributes: Attributes):
        if attributes:
            return dict([(k, self.serialise_content(v))
                         for (k, v) in attributes.items()])

    def serialise_content(self, content):
        if isinstance(content, Element):
            return self.serialise_element(content)
        elif isinstance(content, list):
            return [self.serialise_element(e) for e in content]
        elif isinstance(content, KeyValuePair):
            return [
                "pair",
                self.serialise_element(content.key),
                self.serialise_element(content.value)
            ]

        return content

    def serialise_element(self, element: Element):
        return [
            element.element,
            self.serialise_meta(element.meta),
            self.serialise_attributes(element.attributes),
            self.serialise_content(element.content)
        ]

    def serialise(self, element: Element) -> str:
        """
        Serialises the given element into Compact JSON.

        >>> CompactJSONSerialiser().serialise(String(content='Hello'))
        '["string", null, null, "Hello"]'
        """

        return json.dumps(self.serialise_element(element))


class CompactJSONDeserialiser:
    """
    JSON Refract Deserialiser
    """

    def __init__(self, registry: Registry=None) -> None:
        self.registry = registry or Registry()

    def deserialise_meta(self, meta) -> Metadata:
        metadata = Metadata()

        for key in META_KEYS:
            if meta and key in meta:
                element = self.deserialise_element(meta[key])
                setattr(metadata, key, element)

        return metadata

    def deserialise_attributes(self, attributes) -> dict:
        if attributes:
            return dict([(k, self.deserialise_element(v))
                         for (k, v) in attributes.items()])

        return {}

    def deserialise_element(self, source) -> Element:
        if len(source) != 4:
            raise ValueError('Given element is not tuple of 4')

        element_name = source[0]
        element_cls = self.registry.find_element_class(element_name)
        meta = self.deserialise_meta(source[1])
        attributes = self.deserialise_attributes(source[2])
        element = element_cls(meta=meta, attributes=attributes)
        element.element = element_name

        content = source[3]
        if isinstance(content, list):
            if len(content) == 4 and isinstance(content[0], str):
                element.content = self.deserialise_element(content)
            elif len(content) > 1 and content[0] == 'pair':
                key = self.deserialise_element(content[1])

                if len(content) > 2:
                    value = self.deserialise_element(content[2])
                else:
                    value = None

                element.content = KeyValuePair(key=key, value=value)
            else:
                element.content = [self.deserialise_element(e)
                                   for e in content]
        else:
            element.content = content

        return element

    def deserialise(self, content) -> Element:
        """
        Deserialises the given compact JSON into an element.

        >>> deserialiser = CompactJSONDeserialiser()
        >>> deserialiser.deserialise('["string", null, null, "Hi"]')
        String(content='Hi')
        """

        content = json.loads(content)
        if not isinstance(content, list):
            raise ValueError('Given content was not compact JSON refract')

        return self.deserialise_element(content)
