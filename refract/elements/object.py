from typing import List

from refract.elements.base import Element, Metadata, KeyValuePair


class Member(Element):
    """
    Refract Member Element

    >>> Member(key=Element(), value=Element())
    """

    element = 'member'

    def __init__(self, meta: Metadata = None, attributes = None,
                 key: Element=None, value: Element=None) -> None:
        super(Member, self).__init__('member', meta=meta,
                                     attributes=attributes,
                                     content=KeyValuePair(key, value))

    @property
    def key(self) -> Element:
        """
        The members key element
        """

        return self.content.key

    @key.setter
    def key(self, key: Element):
        from refract.refraction import refract
        self.content = KeyValuePair(key=refract(key), value=self.value)

    @property
    def value(self) -> Element:
        """
        The members value element
        """

        return self.content.value

    @value.setter
    def value(self, value: Element):
        from refract.refraction import refract
        self.content = KeyValuePair(key=self.key, value=refract(value))


class Object(Element):
    """
    Refract Object Element

    >>> Object(content={})

    >>> Object(content=[Member()])
    """

    element = 'object'

    def __init__(self, meta: Metadata = None, attributes = None,
                 content: List[Member] = None) -> None:
        super(Object, self).__init__(meta=meta, attributes=attributes)

        if isinstance(content, (dict)):
            from refract.refraction import refract
            self.content = refract(content).content
        else:
            self.content = content

    def __len__(self):
        """
        Number of items in the object.

        >>> len(Object())
        0
        """

        if self.content:
            return len(self.content)

        return 0

    def __getitem__(self, key) -> Element:
        """
        Returns the value for the given key

        >>> key = String(content='id')
        >>> value = String(content='Hello')
        >>> obj = Object(content=[Member(key=key, value=value)])
        >>> obj['id']
        String(content='Hello')
        """

        if self.content:
            from refract.refraction import refract
            refracted_key = refract(key)

            for member in self.content:
                if member.key == refracted_key:
                    return member.content.value

        raise KeyError(key)

    def __delitem__(self, key):
        """
        Deletes the member for the given key

        >>> key = String(content='id')
        >>> value = String(content='Hello')
        >>> obj = Object(content=[Member(key=key, value=value)])
        >>> del obj[key]
        """

        if self.content:
            from refract.refraction import refract
            refracted_key = refract(key)

            for member in self.content:
                if member.key == refracted_key:
                    member.parent = None
                    self.content.remove(member)
                    return

        raise KeyError(key)

    def __contains__(self, key) -> bool:
        """
        Returns whether the object contains the given key.

        >>> key = String(content='id')
        >>> value = String(content='Hello')
        >>> obj = Object(content=[Member(key=key, value=value)])
        >>> key in obj
        True
        """

        try:
            self[key]
        except KeyError:
            return False

        return True

    def keys(self) -> List[Element]:
        """
        Returns all of the objects keys.
        """

        return [element.key for element in self.content]

    def values(self) -> List[Element]:
        """
        Returns all of the objects values.
        """

        return [element.value for element in self.content]
