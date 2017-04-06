from collections import namedtuple


class Element(object):
    def __init__(self, element: str, content=None):
        self.element = element
        self.content = content

    def as_dict(self) -> dict:
        element = {
            'element': self.element,
        }

        if self.content or self.element == "null":
            if isinstance(self.content, KeyValuePair):
                content = {}

                if self.content.key:
                    content['key'] = self.content.key.as_dict()

                if self.content.value:
                    content['value'] = self.content.value.as_dict()

                element['content'] = content
            elif isinstance(self.content, list):
                element['content'] = [e.as_dict() for e in self.content]
            elif isinstance(self.content, Element):
                element['content'] = self.content.as_dict()
            else:
                element['content'] = self.content

        # TODO meta
        # TODO attributes

        return element

    @classmethod
    def from_dict(cls, namespace, element_dict):
        if 'element' not in element_dict:
            raise ValueError('Given element does not contain an element property')

        if hasattr(cls, 'element'):
            element = cls()
        else:
            element = cls(element_dict['element'])

        if 'content' in element_dict:
            content = element_dict['content']

            if isinstance(content, list):
                element.content = [namespace.from_dict(e) for e in content]
            elif isinstance(content, dict):
                if element.element == 'member':
                    key = content.get('key')
                    if key:
                        element.key = namespace.from_dict(key)

                    value = content.get('value')
                    if value:
                        element.value = namespace.from_dict(value)
                else:
                    element.content = namespace.from_dict(content)
            else:
                element.content = content

        # TODO meta
        # TODO attributes

        return element


class String(Element):
    element = 'string'

    def __init__(self, content=None):
        super(String, self).__init__('string', content=content)


class Number(Element):
    element = 'number'

    def __init__(self, content=None):
        super(Number, self).__init__('number', content=content)


class Boolean(Element):
    element = 'boolean'

    def __init__(self, content=None):
        super(Boolean, self).__init__('boolean', content=content)


class Null(Element):
    element = 'null'

    def __init__(self):
        super(Null, self).__init__('null', content=None)


KeyValuePair = namedtuple('KeyValuePair', ['key', 'value'])
class Member(Element):
    element = 'member'

    def __init__(self, key: Element=None, value: Element=None):
        super(Member, self).__init__('member', KeyValuePair(key, value))

    @property
    def key(self) -> Element:
        return self.content.key

    @key.setter
    def key(self, key: Element):
        self.content = KeyValuePair(key=key, value=self.value)

    @property
    def value(self) -> Element:
        return self.content.value

    @value.setter
    def value(self, value: Element) -> Element:
        self.content = KeyValuePair(key=self.key, value=value)


class Array(Element):
    element = 'array'

    def __init__(self, content=None):
        super(Array, self).__init__('array', content=content)

    def __len__(self):
        return len(self.content)

    def __getitem__(self, index):
        return self.content.__getitem__(index)


class Object(Element):
    element = 'object'

    def __init__(self, content=None):
        super(Object, self).__init__('object', content=content)

    def __len__(self):
        return len(self.content)

    def keys(self):
        return [element.key for element in self.content]

    def values(self):
        return [element.value for element in self.content]
