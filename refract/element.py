from collections import namedtuple


MemberContent = namedtuple('MemberContent', ['key', 'value'])


class Element(object):
    def __init__(self, element, content=None):
        self.element = element
        self.content = content

    def as_dict(self):
        element = {
            'element': self.element,
        }

        if self.content or self.element == "null":
            if isinstance(self.content, MemberContent):
                content = {}

                if self.content.key:
                    content['key'] = self.content.key.as_dict()

                if self.content.value:
                    content['value'] = self.content.value.as_dict()

                element['content'] = content
            elif isinstance(self.content, list):
                element['content'] = map(lambda e: e.as_dict(), self.content)
            elif isinstance(self.content, Element):
                element['content'] = self.content.as_dict()
            else:
                element['content'] = self.content

        # TODO meta
        # TODO attributes

        return element

    def as_tuple(self):
        content = self.content

        if isinstance(self.content, MemberContent):
            content = []

            if self.content.key:
                content.append(self.content.key.as_tuple())

                if self.content.value:
                    content.append(self.content.value.as_tuple())
        elif isinstance(self.content, list):
            content = map(lambda e: e.as_tuple(), self.content)
        elif isinstance(self.content, Element):
            content = self.content.as_tuple()

        # TODO meta
        # TODO attributes

        return [self.element, [], [], content]

    @classmethod
    def from_dict(self, element_dict):
        if 'element' not in element_dict:
            raise ValueError('Given element does not contain an element property')

        element = Element(element_dict['element'])

        if 'content' in element_dict:
            content = element_dict['content']

            if isinstance(content, list):
                element.content = map(Element.from_dict, content)
            elif isinstance(content, dict):
                if element.element == 'member':
                    key = content.get('key')
                    if key:
                        key = Element.from_dict(key)

                    value = content.get('value')
                    if value:
                        value = Element.from_dict(value)

                    element.content = MemberContent(key=key, value=value)
                else:
                    element.content = Element.from_dict(content)
            else:
                element.content = content

        # TODO meta
        # TODO attributes

        return element

    @classmethod
    def from_tuple(self, element_tuple):
        if len(element_tuple) == 0:
            raise ValueError('Invalid element tuple, missing element')

        if len(element_tuple) > 4:
            raise ValueError('Invalid element tuple, too many values')

        element = Element(element_tuple[0])

        if len(element_tuple) > 3:
            content = element_tuple[3]

            if isinstance(content, list) and len(content) > 0:
                if isinstance(content[0], str):
                    element.content = Element.from_tuple(content)
                else:
                    element.content = map(Element.from_tuple, content)
            else:
                element.content = content

        if element.element == 'member' and isinstance(element.content, list):
            element.content = MemberContent(
                key=element.content.pop(0),
                value=element.content.pop(0)
            )

        # TODO meta
        # TODO attributes

        return element
