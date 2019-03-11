from refract.elements.base import Element, Attributes, Metadata


class String(Element):
    """
    Refract String Element

    >>> String(content='Hello')
    """

    element = 'string'

    def __init__(self, meta: Metadata = None, attributes: Attributes = None,
                 content: str = None) -> None:
        super(String, self).__init__(
            meta=meta,
            attributes=attributes,
            content=content
        )

    def __lt__(self, other: Element) -> bool:
        return self.content < other.content


class Number(Element):
    """
    Refract Number Element

    >>> Number(content=5)
    """

    element = 'number'

    def __init__(self, meta: Metadata = None, attributes: Attributes = None,
                 content=None) -> None:
        super(Number, self).__init__(
            meta=meta,
            attributes=attributes,
            content=content
        )

    def __lt__(self, other: Element) -> bool:
        return self.content < other.content


class Boolean(Element):
    """
    Refract Boolean Element

    >>> Boolean(content=True)
    """

    element = 'boolean'

    def __init__(self, meta: Metadata = None, attributes: Attributes = None,
                 content: bool = None) -> None:
        super(Boolean, self).__init__(
            meta=meta,
            attributes=attributes,
            content=content
        )


class Null(Element):
    """
    Refract Null Element

    >>> Null()
    """

    element = 'null'

    def __init__(self, meta: Metadata = None,
                 attributes: Attributes = None) -> None:
        super(Null, self).__init__(meta=meta, attributes=attributes)
