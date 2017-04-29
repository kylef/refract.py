from refract.elements.base import Element, Metadata


class Array(Element):
    element = 'array'

    def __init__(self, meta: Metadata = None, attributes=None, content=None):
        super(Array, self).__init__('array', meta=meta, attributes=attributes, content=content)

    def __len__(self):
        if self.content:
            return len(self.content)

        return 0

    def __getitem__(self, index):
        return self.content.__getitem__(index)

    def append(self, element):
        self.content.append(element)

