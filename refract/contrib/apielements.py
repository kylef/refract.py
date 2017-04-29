from typing import List

from refract.elements import Array, String, Number
from refract.namespace import Namespace


__all__ = [
    'namespace', 'ParseResult', 'Annotation', 'Category', 'Copy', 'Resource',
    'Transition', 'HTTPTransaction', 'HTTPRequest', 'HTTPResponse', 'Asset'
]


namespace = Namespace()


def has_class(class_name):
    def func(element):
        return element.classes and class_name in element.classes

    return func


def is_element(element_cls):
    def func(element):
        return isinstance(element, element_cls)

    return func


@namespace.register
class Annotation(String):
    element = 'annotation'


@namespace.register
class Copy(String):
    element = 'copy'


@namespace.register
class Asset(String):
    element = 'asset'

    @property
    def content_type(self) -> String:
        """
        The content type of the asset
        """
        return self.attributes.get('contentType', None)

    @content_type.setter
    def content_type(self, new_value: String):
        self.attributes['contentType'] = new_value


class HTTPMessage(Array):
    @property
    def headers(self):
        """
        Returns the header attributes for the HTTP message.
        """

        return self.attributes.get('headers', None)

    @property
    def assets(self) -> List[Asset]:
        """
        Returns the assets in the transaction.
        """

        return list(filter(is_element(Asset), self.content))

    @property
    def body_asset(self) -> Asset:
        """
        Returns the first body asset in the transaction.
        """

        return next(filter(has_class('messageBody'), self.assets))

    @property
    def body_schema_asset(self) -> Asset:
        """
        Returns the first body schema asset in the transaction.
        """

        return next(filter(has_class('messageBodySchema'), self.assets))


@namespace.register
class HTTPRequest(HTTPMessage):
    element = 'httpRequest'

    @property
    def method(self) -> String:
        """
        Returns the method attributes for the HTTP request.
        """

        return self.attributes.get('method', None)


@namespace.register
class HTTPResponse(HTTPMessage):
    element = 'httpResponse'

    @property
    def status_code(self) -> Number:
        """
        Returns the statuc code attribute for the HTTP response.
        """

        return self.attributes.get('statusCode', None)


@namespace.register
class HTTPTransaction(Array):
    element = 'httpTransaction'

    @property
    def request(self) -> HTTPRequest:
        """
        Returns the first HTTPRequest in the transaction.
        """

        return next(filter(is_element(HTTPRequest), self.content))

    @property
    def response(self) -> HTTPResponse:
        """
        Returns the first HTTPResponse in the transaction.
        """

        return next(filter(is_element(HTTPResponse), self.content))


@namespace.register
class Transition(Array):
    element = 'transition'

    @property
    def transactions(self) -> List[HTTPTransaction]:
        """
        Returns the HTTP transactions inside the transition.
        """

        return list(filter(is_element(HTTPTransaction), self.content))


@namespace.register
class Resource(Array):
    element = 'resource'

    @property
    def transitions(self) -> List[Transition]:
        """
        Returns the transitions inside the resource.
        """

        return list(filter(is_element(Transition), self.content))


@namespace.register
class Category(Array):
    element = 'category'

    @property
    def resourceGroups(self) -> List[Array]:
        """
        Returns the resource group categories found within the category.
        """

        categories = filter(is_element(Category), self.children)
        resourceGroups = filter(has_class('resourceGroup'), categories)
        return list(resourceGroups)

    @property
    def resources(self) -> List[Resource]:
        """
        Returns the resource elements found within the category.
        """

        return list(filter(is_element(Resource), self.children))

    @property
    def transitions(self) -> List[Transition]:
        """
        Returns the transition elements found within the category.
        """

        return list(filter(is_element(Transition), self.children))


@namespace.register
class ParseResult(Array):
    element = 'parseResult'

    @property
    def annotations(self):
        """
        Returns all of the annotations inside the parse result.
        """

        return list(filter(is_element(Annotation), self.children))

    @property
    def warnings(self):
        """
        Returns all of the warning annotations in the parse result.
        """

        return list(filter(has_class('warning'), self.annotations))

    @property
    def errors(self):
        """
        Returns all of the error annotations in the parse result.
        """

        return list(filter(has_class('error'), self.annotations))

    @property
    def api(self) -> Category:
        """
        Returns an API category found within the parse result.
        """

        categories = filter(is_element(Category), self.children)
        apis = filter(has_class('api'), categories)
        return next(apis)
