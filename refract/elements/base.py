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


class Element(object):
    def __init__(self, element: str = None, meta: Metadata = None,
                 attributes = None, content=None) -> None:
        if element and not hasattr(self, 'element'):
            self.element = element
        self.meta = meta or Metadata()
        self.attributes = attributes or {}
        self.content = content

    def __repr__(self):
        if isinstance(self.content, Element):
            return "<Element({}) content={}>".format(self.element, 'Element')

        return "<Element({}) content={}>".format(
            self.element, repr(self.content)
        )

    @property
    def underlying_value(self):
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
        self.meta.id = new_value

    @property
    def title(self):
        return self.meta.title

    @title.setter
    def title(self, new_value):
        self.meta.title = new_value

    @property
    def description(self):
        return self.meta.description

    @description.setter
    def description(self, new_value):
        self.meta.description = new_value

    @property
    def ref(self):
        return self.meta.ref

    @ref.setter
    def ref(self, new_value):
        self.meta.ref = new_value

    @property
    def links(self):
        return self.meta.links

    @links.setter
    def links(self, new_value):
        self.meta.links = new_value

    @property
    def classes(self):
        return self.meta.classes

    @classes.setter
    def classes(self, new_value):
        self.meta.classes = new_value
