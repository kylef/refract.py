from refract.elements.base import Element, Metadata


class String(Element):
    element = 'string'

    def __init__(self, meta: Metadata = None, attributes = None,
                 content: str = None) -> None:
        super(String, self).__init__(
            meta=meta,
            attributes=attributes,
            content=content
        )


class Number(Element):
    element = 'number'

    def __init__(self, meta: Metadata = None, attributes = None,
                 content = None) -> None:
        super(Number, self).__init__(
            meta=meta,
            attributes=attributes,
            content=content
        )


class Boolean(Element):
    element = 'boolean'

    def __init__(self, meta: Metadata = None, attributes = None,
                 content: bool = None) -> None:
        super(Boolean, self).__init__(
            meta=meta,
            attributes=attributes,
            content=content
        )


class Null(Element):
    element = 'null'

    def __init__(self, meta: Metadata = None, attributes = None) -> None:
        super(Null, self).__init__(meta=meta, attributes=attributes)
