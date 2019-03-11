from refract.elements.base import Element, Metadata, Attributes


class Array(Element):
    """
    Refract Object Element

    >>> Array(content=['Hello'])

    >>> Array(content=[Element()])
    """

    element = 'array'

    def __init__(self, meta: Metadata = None, attributes: Attributes = None,
                 content=None) -> None:
        super(Array, self).__init__(meta=meta, attributes=attributes,
                                    content=[])

        if content:
            from refract.refraction import refract
            self.content = list(map(refract, content))

    def __len__(self):
        """
        Number of items in the array.

        >>> len(Array())
        0
        """

        if self.content:
            return len(self.content)

        return 0

    def __getitem__(self, index: int):
        """
        Returns the element at the given index.

        >>> array = Array(content=[String(content='Hello')])
        >>> array[0]
        String(content='Hello')
        """

        return self.content.__getitem__(index)

    def __delitem__(self, index: int):
        """
        >>> array = Array(content=[Element()])
        >>> del array[0]
        """

        del self.content[index]

    def __contains__(self, element) -> bool:
        from refract.refraction import refract
        return refract(element) in self.content

    def append(self, element):
        """
        Append an element onto the array.

        >>> array = Array()
        >>> array.append('test')
        """

        from refract.refraction import refract
        self.content.append(refract(element))

    def insert(self, index: int, element):
        """
        Insert an element at a given position.

        >>> array = Array()
        >>> array.insert(0, Element())
        """

        from refract.refraction import refract
        self.content.insert(index, refract(element))

    def index(self, element: Element) -> int:
        """
        Return the index in the array of the first item whose value is element.
        It is an error if there is no such item.

        >>> element = String('hello')
        >>> array = Array(content=[element])
        >>> array.index(element)
        0
        """

        from refract.refraction import refract
        return self.content.index(refract(element))

    def clear(self):
        """
        Removes all the elements from the array.
        """

        self.content.clear()
