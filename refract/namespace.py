from refract.element import Element


class Namespace(object):
    def from_dict(self, dictionary):
        return Element.from_dict(dictionary)
