from refract.elements import (Number, String, Boolean, Null, Member,
                              Array, Object)


class Registry(object):
    """
    A Refract Registry contains a collection of element classes which can be
    used for deserialising serialised Refract into specialised element
    subclasses.

    By default, the registry contains all primitive Refract types including
    `Array`, `Member`, and `Object`.

    >>> registry = Registry()
    """

    def __init__(self):
        self.elements = [Number, String, Boolean, Null, Member, Array, Object]

    def register(self, element):
        """
        Register a new class in the registry.

        >>> class Request(Element):
        ...     element = 'request'
        >>>
        >>> registry.register(Request)

        Register can be used as class a decorator to register an Element.

        >>> @registry.register
        >>> class Request(Element):
        ...     element = 'request'
        """

        self.elements.append(element)
        return element
