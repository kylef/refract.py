from refract.elements.base import Element, Metadata


class Array(Element):
    """
    Refract Object Element

    >>> Array(content=[Element()])
    """

    element = 'array'

    def __init__(self, meta: Metadata = None, attributes=None,
                 content = None) -> None:
        super(Array, self).__init__(meta=meta, attributes=attributes,
                                    content=content)

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

    def append(self, element: Element):
        """
        Append an element onto the array.

        >>> array = Array()
        >>> array.append(Element())
        """

        self.content.append(element)

    def insert(self, index: int, element: Element):
        """
        Insert an element at a given position.

        >>> array = Array()
        >>> array.insert(0, Element())
        """

        self.content.insert(index, element)

    def index(self, element: Element) -> int:
        """
        Return the index in the array of the first item whose value is element.
        It is an error if there is no such item.

        >>> element = String('hello')
        >>> array = Array(content=[element])
        >>> array.index(element)
        0
        """

        return self.content.index(element)

    def clear(self):
        """
        Removes all the elements from the array.
        """

        self.content.clear()
