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

    @property
    def id(self):
        return self.meta.id

    @id.setter
    def id(self, new_value):
        self.meta.id = new_valid

    @property
    def title(self):
        return self.meta.title

    @title.setter
    def title(self, new_value):
        self.meta.title = new_valid

    @property
    def description(self):
        return self.meta.description

    @description.setter
    def description(self, new_value):
        self.meta.description = new_valid

    @property
    def ref(self):
        return self.meta.ref

    @ref.setter
    def ref(self, new_value):
        self.meta.ref = new_valid

    @property
    def links(self):
        return self.meta.links

    @links.setter
    def links(self, new_value):
        self.meta.links = new_valid

    @property
    def classes(self):
        return self.meta.classes

    @classes.setter
    def classes(self, new_value):
        self.meta.classes = new_valid


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
