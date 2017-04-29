import json

from refract.namespace import Namespace
from refract.elements import Element, Metadata, KeyValuePair


class JSONSerialiser:
    def __init__(self):
        pass

    def serialise_dict(self, element):
        element_dict = {
            'element': element.element,
        }

        meta = {}

        if element.meta.id:
            meta['id'] = self.serialise_dict(element.meta.id)

        if element.meta.title:
            meta['title'] = self.serialise_dict(element.meta.title)

        if element.meta.description:
            meta['description'] = self.serialise_dict(element.meta.description)

        if element.meta.classes:
            meta['classes'] = self.serialise_dict(element.meta.classes)

        if element.meta.links:
            meta['links'] = self.serialise_dict(element.meta.links)

        if element.meta.ref:
            meta['ref'] = self.serialise_dict(element.meta.ref)

        if meta:
            element_dict['meta'] = meta

        if element.attributes:
            element_dict['attributes'] = dict(
                [(k, self.serialise_dict(v))
                    for (k, v) in element.attributes.items()]
            )

        if element.content or element.element == "null":
            if isinstance(element.content, KeyValuePair):
                content = {}

                if element.content.key:
                    content['key'] = self.serialise_dict(element.content.key)

                if element.content.value:
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

    def serialise(self, element, **kwargs):
        return json.dumps(self.serialise_dict(element), **kwargs)


class JSONDeserialiser:
    def __init__(self, namespace=None):
        self.namespace = namespace or Namespace()

    def find_element_class(self, element_name):
        for element in self.namespace.elements:
            if element.element == element_name:
                return element

        return Element

    def deserialise_meta(self, element_dict):
        meta = Metadata()

        if 'meta' in element_dict:
            if 'id' in element_dict['meta']:
                meta.id = self.deserialise_dict(element_dict['meta']['id'])

            if 'title' in element_dict['meta']:
                meta.title = self.deserialise_dict(
                    element_dict['meta']['title']
                )

            if 'description' in element_dict['meta']:
                meta.description = self.deserialise_dict(
                    element_dict['meta']['description']
                )

            if 'ref' in element_dict['meta']:
                meta.ref = self.deserialise_dict(element_dict['meta']['ref'])

            if 'classes' in element_dict['meta']:
                meta.classes = self.deserialise_dict(
                    element_dict['meta']['classes']
                )

            if 'links' in element_dict['meta']:
                meta.links = self.deserialise_dict(
                    element_dict['meta']['links']
                )

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

        cls = self.find_element_class(element_dict['element'])

        if hasattr(cls, 'element'):
            element = cls()
        else:
            element = cls(element_dict['element'])

        element.content = self.deserialise_content(element_dict)
        element.meta = self.deserialise_meta(element_dict)
        element.attributes = self.deserialise_attributes(element_dict)
        return element

    def deserialise(self, element_json):
        return self.deserialise_dict(json.loads(element_json))
