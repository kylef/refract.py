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
