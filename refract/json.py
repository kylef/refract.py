import json
from refract.element import KeyValuePair, Element


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
            element_dict['attributes'] = dict([(k, self.serialise_dict(v)) for (k, v) in element.attributes.items()])

        if element.content or element.element == "null":
            if isinstance(element.content, KeyValuePair):
                content = {}

                if element.content.key:
                    content['key'] = self.serialise_dict(element.content.key)

                if element.content.value:
                    content['value'] = self.serialise_dict(element.content.value)

                element_dict['content'] = content
            elif isinstance(element.content, list):
                element_dict['content'] = [self.serialise_dict(e) for e in element.content]
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

    def deserialise_dict(self, element_dict):
        if 'element' not in element_dict:
            raise ValueError('Given element does not contain an element property')

        cls = self.find_element_class(element_dict['element'])

        if hasattr(cls, 'element'):
            element = cls()
        else:
            element = cls(element_dict['element'])

        if 'content' in element_dict:
            content = element_dict['content']

            if isinstance(content, list):
                element.content = [self.deserialise_dict(e) for e in content]
            elif isinstance(content, dict):
                if element.element == 'member':
                    key = content.get('key')
                    if key:
                        element.key = self.deserialise_dict(key)

                    value = content.get('value')
                    if value:
                        element.value = self.deserialise_dict(value)
                else:
                    element.content = self.deserialise_dict(content)
            else:
                element.content = content

        # TODO meta
        # TODO attributes

        return element

    def deserialise(self, element_json):
        return self.deserialise_dict(json.loads(element_json))
