Python Refract
==============

A library for interacting with Refract_ in Python 3.

Refract provides the ability to take a normal data structure and add a layer on
top of it for the purpose of annotating and adding semantic data.

.. code-block:: python

  >>> element = refract({'name': 'Doe', 'email': 'doe@example.com'})
  >>> element.title = 'Person'
  >>> element['email'].classes.append('personal')

Installation
------------

To install Python Refract, simply run this simple command in your terminal of choice.

.. code-block:: shell

  $ pip install refract

API Documentation
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   elements
   serialisers
   apielements

.. _Refract: https://github.com/refractproject/refract-spec
