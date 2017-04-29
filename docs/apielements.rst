.. _apielements:

API Elements
============

Python Refact contains a namespace for the `API Elements`_ Refract Profile
which provide conviences around interacting with API Elements.

.. code-block:: python

    from refract.json import JSONDeserialiser
    from refract.contrib.apielements import namespace

    deserialiser = JSONDeserialiser(namespace=namespace)
    parseResult = deserialiser.deserialise('{"element": "parseResult"}')

    if parseResult.errors:
        print('Parse Result contained errors')

.. _API Elements: http://api-elements.readthedocs.io

.. contents::
  :depth: 3

.. module:: refract.contrib.apielements

ParseResult
-----------

.. autoclass:: ParseResult
   :members:

Annotation
----------

.. autoclass:: Annotation
   :members:

Category
--------

.. autoclass:: Category
   :members:

Copy
----

.. autoclass:: Copy
   :members:

Resource
--------

.. autoclass:: Resource
   :members:

Transition
----------

.. autoclass:: Transition
   :members:

HTTPTransaction
---------------

.. autoclass:: HTTPTransaction
   :members:

HTTPRequest
-----------

.. autoclass:: HTTPRequest
   :members: method, headers, assets, body_asset, body_schema_asset

HTTPResponse
------------

.. autoclass:: HTTPResponse
   :members: status_code, headers, assets, body_asset, body_schema_asset

Asset
-----

.. autoclass:: Asset
   :members:
