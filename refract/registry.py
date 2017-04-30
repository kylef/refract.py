from refract.elements import (Element, Number, String, Boolean, Null,
                              Member, Array, Object)


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

    def find_element_class(self, element_name):
        """
        Finds an element class for the given element name contained within the
        registry.

        Returns Element when there is no matching element subclass.

        >>> registry.find_element_class('string')
        String

        >>> registry.find_element_class('unknown')
        Element
        """

        for element in self.elements:
            if element.element == element_name:
                return element

        return Element
