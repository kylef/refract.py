from refract.elements.base import Element, Metadata, KeyValuePair


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



class Object(Element):
    element = 'object'

    def __init__(self, meta: Metadata = None, attributes = None, content=None):
        super(Object, self).__init__('object', meta=meta, attributes=attributes, content=content)

    def __len__(self):
        if self.content:
            return len(self.content)

        return 0

    def keys(self):
        return [element.key for element in self.content]

    def values(self):
        return [element.value for element in self.content]
