# Refract Python Changelog

## 0.4.0 (2019-04-08)

### Breaking

- Python 3.5 support has been dropped.

### Bug Fixes

- JSON deserialisation will now deserialise attributes as Attributes object.  
  [#4](https://github.com/kylef/refract.py/issues/4)

## 0.3.1 (2017-06-02)

### Enhancements

- Added convenience accessors `href` to Resource, Transition, HTTPRequest
  elements.

### Bug Fixes

- JSON Serialise will now serialise empty arrays when they are found within a
  key value pair or inside meta properties.


## 0.3.0 (2017-05-03)

### Breaking

- Namespace has been renamed to Registry.

### Enhancements

- Added a compact JSON serialiser.
- Added a compact JSON deserialiser.
- Elements repr will now use an elements class name if the element is a
  subclass.

## 0.2.0 (2017-04-29)

### Enhancements

- Added [API Elements](http://api-elements.readthedocs.io) Profile.


## 0.1.0 (2017-04-28)

Initial Release.
