from typing import List

from refract.elements.base import Element, Metadata, KeyValuePair
from refract.elements.array import Array


class Member(Element):
    element = 'member'

    def __init__(self, meta: Metadata = None, attributes = None,
                 key: Element=None, value: Element=None) -> None:
        super(Member, self).__init__('member', meta=meta,
                                     attributes=attributes,
                                     content=KeyValuePair(key, value))

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
    def value(self, value: Element):
        self.content = KeyValuePair(key=self.key, value=value)


class Object(Array):
    element = 'object'

    def __init__(self, meta: Metadata = None, attributes = None,
                 content: List[Member] = None) -> None:
        super(Object, self).__init__(meta=meta, attributes=attributes,
                                     content=content)

    def keys(self) -> List[Element]:
        return [element.key for element in self.content]

    def values(self) -> List[Element]:
        return [element.value for element in self.content]
