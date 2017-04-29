from refract.elements import (Element, String, Number, Boolean, Null, Array,
                              Object, Member)


__all__ = ('refract',)


def refract(structure) -> Element:
    """
    Refracts the given value.

    >>> refract('string')
    String(content='string')

    >>> refract(1)
    Number(content=1)

    >>> refract(True)
    Boolean(content=True)

    >>> refract(None)
    Null()

    >>> refract([1, 2])
    Array(content=[Number(content=1), Number(content=2)])

    >>> refract({'name': 'Doe'})
    Object(content=[Member(
        key=String(content='name'),
        value=String(content='Doe')
    )])
    """

    if isinstance(structure, Element):
        return structure
    elif isinstance(structure, str):
        return String(content=structure)
    elif isinstance(structure, bool):
        return Boolean(content=structure)
    elif isinstance(structure, (int, float)):
        return Number(content=structure)
    elif isinstance(structure, (list, tuple)):
        return Array(content=list(map(refract, structure)))
    elif isinstance(structure, dict):
        return Object(content=[Member(key=refract(k), value=refract(v))
                               for (k, v) in structure.items()])
    elif structure is None:
        return Null()

    raise ValueError('Unsupported Value Type')
