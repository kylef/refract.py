from refract.element import Element, Number, String, Boolean, Null, Member, Array, Object


class Namespace(object):
    def __init__(self):
        self.elements = [Number, String, Boolean, Null, Member, Array, Object]

    def from_dict(self, dictionary):
        for element in self.elements:
            if element.element == dictionary['element']:
                return element.from_dict(self, dictionary)

        return Element.from_dict(self, dictionary)
