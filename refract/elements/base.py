from collections import namedtuple


KeyValuePair = namedtuple('KeyValuePair', ['key', 'value'])


class Metadata:
    def __init__(self, id = None, title = None, description = None,
                 classes = None, links = None, ref = None) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.classes = classes
        self.links = links
        self.ref = ref

    def __eq__(self, other):
        if not isinstance(other, Metadata):
            return False

        return (
            self.id == other.id and
            self.title == other.title and
            self.description == other.description and
            self.classes == other.classes and
            self.links == other.links and
            self.ref == other.ref
        )


class Attributes:
    def __init__(self):
        self.attributes = {}

    def __eq__(self, other):
        if not isinstance(other, Attributes):
            return False

        return self.attributes == other.attributes

    def __len__(self):
        return self.attributes.__len__()

    def __getitem__(self, item):
        return self.attributes.__getitem__(item)

    def __setitem__(self, item, value):
        from refract.refraction import refract
        value = refract(value)
        self.attributes.__setitem__(item, value)

    def items(self):
        return self.attributes.items()

    def keys(self):
        return self.attributes.keys()

    def values(self):
        return self.attributes.values()

    def get(self, *args, **kwargs):
        return self.attributes.get(*args, **kwargs)


class Element(object):
    """
    Base Refract Element
    """

    def __init__(self, element: str = None, meta: Metadata = None,
                 attributes: Attributes = None, content=None) -> None:
        if element and not hasattr(self, 'element'):
            self.element = element
        self.meta = meta or Metadata()
        self.attributes = attributes or Attributes()
        self.content = content

    def __repr__(self):
        if isinstance(self.content, Element):
            return "<Element({}) content={}>".format(self.element, 'Element')

        return "<Element({}) content={}>".format(
            self.element, repr(self.content)
        )

    def __eq__(self, other):
        if not isinstance(other, Element):
            return False

        return (
            self.element == other.element and
            self.meta == other.meta and
            self.attributes == other.attributes and
            self.content == other.content
        )

    @property
    def defract(self):
        """
        Returns the underlying (unrefracted) value of element

        >>> Element(content='Hello').defract
        'Hello'

        >>> Element(content=Element(content='Hello')).defract
        'Hello'

        >>> Element(content=[Element(content='Hello')]).defract
        ['Hello']
        """

        from refract.elements.object import Object

        def get_value(item):
            if isinstance(item, KeyValuePair):
                return (get_value(item.key), get_value(item.value))
            elif isinstance(item, list):
                return [get_value(element) for element in item]
            elif isinstance(item, Element):
                if isinstance(item, Object) or item.element == 'object':
                    return dict(get_value(item.content))
                return get_value(item.content)

            return item

        return get_value(self)

    # Meta Accessors

    @property
    def id(self):
        return self.meta.id

    @id.setter
    def id(self, new_value):
        from refract.refraction import refract
        self.meta.id = refract(new_value)

    @property
    def title(self):
        return self.meta.title

    @title.setter
    def title(self, new_value):
        from refract.refraction import refract
        self.meta.title = refract(new_value)

    @property
    def description(self):
        return self.meta.description

    @description.setter
    def description(self, new_value):
        from refract.refraction import refract
        self.meta.description = refract(new_value)

    @property
    def ref(self):
        return self.meta.ref

    @ref.setter
    def ref(self, new_value):
        from refract.refraction import refract
        self.meta.ref = refract(new_value)

    @property
    def links(self):
        return self.meta.links

    @links.setter
    def links(self, new_value):
        from refract.refraction import refract
        self.meta.links = refract(new_value)

    @property
    def classes(self):
        return self.meta.classes

    @classes.setter
    def classes(self, new_value):
        from refract.refraction import refract
        self.meta.classes = refract(new_value)

    #

    @property
    def children(self):
        """
        Returns all of the children elements.
        """

        if isinstance(self.content, list):
            return self.content
        elif isinstance(self.content, Element):
            return [self.content]
        else:
            return []

    @property
    def recursive_children(self):
        """
        Generator returning all recursive children elements.
        """

        for child in self.children:
            yield child

            for recursive_child in child.recursive_children:
                yield recursive_child
