from collections import namedtuple


class Metadata:
    def __init__(self, id = None, title = None, description = None, classes = None, links = None, ref = None):
        self.id = id
        self.title = title
        self.description = description
        self.classes = classes
        self.links = links
        self.ref = ref


class Element(object):
    def __init__(self, element: str, meta: Metadata = None, attributes = None, content=None):
        self.element = element
        self.meta = meta or Metadata()
        self.attributes = attributes or {}
        self.content = content

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

    def __init__(self, meta: Metadata = None, attributes = None, content=None):
        super(String, self).__init__('string', meta=meta, attributes=attributes, content=content)


class Number(Element):
    element = 'number'

    def __init__(self, attributes = None, content=None):
        super(Number, self).__init__('number', attributes=attributes, content=content)


class Boolean(Element):
    element = 'boolean'

    def __init__(self, meta: Metadata = None, attributes = None, content=None):
        super(Boolean, self).__init__('boolean', meta=meta, attributes=attributes, content=content)


class Null(Element):
    element = 'null'

    def __init__(self, meta: Metadata = None):
        super(Null, self).__init__('null', meta=meta, content=None)


KeyValuePair = namedtuple('KeyValuePair', ['key', 'value'])
class Member(Element):
    element = 'member'

    def __init__(self, meta: Metadata = None, attributes = None, key: Element=None, value: Element=None):
        super(Member, self).__init__('member', meta=meta, attributes=attributes, content=KeyValuePair(key, value))

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

    def __init__(self, meta: Metadata = None, attributes=None, content=None):
        super(Array, self).__init__('array', meta=meta, attributes=attributes, content=content)

    def __len__(self):
        return len(self.content)

    def __getitem__(self, index):
        return self.content.__getitem__(index)


class Object(Element):
    element = 'object'

    def __init__(self, meta: Metadata = None, attributes = None, content=None):
        super(Object, self).__init__('object', meta=meta, attributes=attributes, content=content)

    def __len__(self):
        return len(self.content)

    def keys(self):
        return [element.key for element in self.content]

    def values(self):
        return [element.value for element in self.content]
