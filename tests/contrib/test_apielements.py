import unittest
from refract.elements import String, Number
from refract.contrib.apielements import (
    ParseResult, Annotation, Category, Copy, Resource, Asset, HTTPRequest,
    HTTPResponse, HTTPTransaction, Transition
)


class ParseResultTests(unittest.TestCase):
    def setUp(self):
        self.parseResult = ParseResult()
        self.parseResult.append(Category())
        self.parseResult.append(Annotation(content='warn!'))
        self.parseResult.append(Annotation(content='err!'))

        self.parseResult[0].classes = ['api']
        self.parseResult[1].classes = ['warning']
        self.parseResult[2].classes = ['error']

    def test_element_name(self):
        self.assertEqual(self.parseResult.element, 'parseResult')

    def test_annotations(self):
        self.assertEqual(len(self.parseResult.annotations), 2)
        self.assertEqual(self.parseResult.annotations[0].content, 'warn!')
        self.assertEqual(self.parseResult.annotations[1].content, 'err!')

    def test_warnings(self):
        self.assertEqual(len(self.parseResult.warnings), 1)
        self.assertEqual(self.parseResult.warnings[0].content, 'warn!')

    def test_errors(self):
        self.assertEqual(len(self.parseResult.errors), 1)
        self.assertEqual(self.parseResult.errors[0].content, 'err!')

    def test_api(self):
        self.assertEqual(self.parseResult.api.element, 'category')


class AnnotationTests(unittest.TestCase):
    def test_element_name(self):
        annotation = Annotation()
        self.assertEqual(annotation.element, 'annotation')


class CategoryTests(unittest.TestCase):
    def setUp(self):
        self.category = Category()

    def test_element_name(self):
        self.assertEqual(self.category.element, 'category')


class ResourceTests(unittest.TestCase):
    def setUp(self):
        self.resource = Resource(content=[
            Transition()
        ])

    def test_element_name(self):
        self.assertEqual(self.resource.element, 'resource')

    def test_transitions(self):
        self.assertEqual(len(self.resource.transitions), 1)
        self.assertIsInstance(self.resource.transitions[0], Transition)


class TransitionTests(unittest.TestCase):
    def setUp(self):
        self.transition = Transition(content=[
            HTTPTransaction()
        ])

    def test_element_name(self):
        self.assertEqual(self.transition.element, 'transition')

    def test_transactions(self):
        self.assertEqual(len(self.transition.transactions), 1)
        self.assertIsInstance(self.transition.transactions[0], HTTPTransaction)


class HTTPTransactionTests(unittest.TestCase):
    def setUp(self):
        self.transaction = HTTPTransaction(content=[
            Copy(),
            HTTPRequest(),
            HTTPResponse()
        ])

    def test_element_name(self):
        self.assertEqual(self.transaction.element, 'httpTransaction')

    def test_request(self):
        self.assertEqual(self.transaction.request.element, 'httpRequest')

    def test_response(self):
        self.assertEqual(self.transaction.response.element, 'httpResponse')


class HTTPRequestTests(unittest.TestCase):
    def setUp(self):
        self.request = HTTPRequest(content=[
            Asset()
        ])
        self.request.attributes['method'] = String(content='GET')

    def test_element_name(self):
        self.assertEqual(self.request.element, 'httpRequest')

    def test_method(self):
        self.assertEqual(self.request.method.content, 'GET')

    def test_assets(self):
        self.assertEqual(self.request.assets[0].element, 'asset')


class HTTPResponseTests(unittest.TestCase):
    def setUp(self):
        self.response = HTTPResponse(content=[
            Asset()
        ])
        self.response.attributes['statusCode'] = Number(content=200)

    def test_element_name(self):
        self.assertEqual(self.response.element, 'httpResponse')

    def test_status_code(self):
        self.assertEqual(self.response.status_code.content, 200)

    def test_assets(self):
        self.assertEqual(self.response.assets[0].element, 'asset')


class AssetTests(unittest.TestCase):
    def setUp(self):
        self.asset = Asset()
        self.asset.attributes['contentType'] = String(
            content='application/example'
        )

    def test_element_name(self):
        self.assertEqual(self.asset.element, 'asset')

    def test_get_content_type(self):
        self.assertEqual(self.asset.content_type.content,
                         'application/example')

    def test_set_content_type(self):
        self.asset.content_type = String(content='hello')
        self.assertEqual(self.asset.attributes['contentType'].content, 'hello')
