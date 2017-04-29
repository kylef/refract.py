import sys
from refract.json import JSONDeserialiser, JSONSerialiser
from serialiser import LegacyJSONDeserialiser, PrettyJSONSerialiser

paths = sys.argv[1:]
if paths:
    for path in paths:
        with open(path) as fp:
            element = LegacyJSONDeserialiser().deserialise(fp.read())
            print(element)
            print(PrettyJSONSerialiser().serialise(element))
