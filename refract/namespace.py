from refract.element import Element, Number, String, Boolean, Null, Member, Array, Object


class Namespace(object):
    def __init__(self):
        self.elements = [Number, String, Boolean, Null, Member, Array, Object]
