from refract.elements import (Number, String, Boolean, Null, Member,
                              Array, Object)


class Namespace(object):
    def __init__(self):
        self.elements = [Number, String, Boolean, Null, Member, Array, Object]

    def register(self, element):
        self.elements.append(element)
        return element
