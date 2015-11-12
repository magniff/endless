# RESTACK

This tiny library helps you to write recoursive functions without any ''stack overflow'' related pain.

Say you have a function like this:
```python
def factorial(value):
	return 1 if value == 1 else value * factorial(value-1)
```
It works fine untill the ```value``` thing is less then a ```sys.getrecursionlimit()```.

RESTACK provides a solution (stolen from Dave Beazley, really)
```python
@restack.decorate
def factorial(value):
	return 1 if value == 1 else value * (yield {'value': value-1})
```
the last one is completely stack overflow free, see tests for more insight.

Also stuff like this one is also possible (called maccarthy91 function):
```python
@restack.decorate
def maccarthy(value):
    if value > 100:
        return value - 10
    else:
        return (yield {'value': (yield {'value': value+11})})
```
