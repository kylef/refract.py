# Refract Python

A Python library for interacting with
[Refract](https://github.com/refractproject/refract-spec).

## Installation

```shell
$ pip install refract
```

## Usage

### Elements

#### Base Element

```python
element = Element('elementName', content='Doe')
```

##### Meta Accessors

```python
element.id = String(content='Doe')
element.title = String(content='Name')
element.description = String(content='A short decription')
```

##### Defract

You can compute the underlying value into a Python type using
`defract`.

```python
element = Object(content=[
  Member(key=String(content='id'), value=String(content='Example'))
])

print(element.defract)
# {'id': 'Example'}
```

#### String

```python
element = String(content='Doe')
```

#### Number

```python
element = Number(content=7)
```

#### Boolean

```python
element = Boolean(content=True)
```

#### Null

```python
element = Null()
```

#### Array

```python
array = Array(content=[
  String(content='Doe')
])

array.append(String(content='Other'))
```

##### `len`

```python
len(array)
```

##### Subscript

```python
array[0]
# String(content='Doe')
```

##### Iteration

```python
for element in array:
    print(element)
```

You can use high order functions like map, filter, reduce on array.

```python
strings = filter(lambda element: element is String, array)
```

#### Member

```python
member = Member(key=String(content='id'), value=String(content='Example'))

member.key
# String(content='id')

member.value
# String(content='Example')
```

#### Object

```python
obj = Object(content=[
  Member(key=String(content='id'), value=String(content='Example'))
])
```

##### `len`

```python
len(obj)
```

##### `keys`

```python
obj.keys()
# [String(content='id')]
```

##### `values`

```python
obj.values()
# [String(content='Example')]
```

#### KeyValuePair

```python
pair = KeyValuePair(key=String(content='id'), value=String(content='Example'))
```

### Serialisation

```python
from refract.json import JSONSerialiser, JSONDeserialiser

serialiser = JSONSerialiser()
json = serialiser.serialise(element)

deserialiser = JSONDeserialiser()
element = deserialiser.deserialise(json)
```
