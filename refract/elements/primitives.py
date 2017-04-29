from refract.elements.base import Element, Metadata


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

