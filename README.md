# Refract Python

A library for interacting with
[Refract](https://github.com/refractproject/refract-spec) in Python 3.

Refract provides the ability to take a normal data structure and add a layer on
top of it for the purpose of annotating and adding semantic data.

```python
>>> element = refract({'name': 'Doe', 'email': 'doe@example.com'})
>>> element.title = 'Person'
>>> element['email'].classes.append('personal')
```

## Installation

To install Python Refract, simply run this simple command in your terminal of choice.

```shell
$ pip install refract
```

## Documentation

Documentation is available at
[http://python-refract.readthedocs.io](http://python-refract.readthedocs.io).
