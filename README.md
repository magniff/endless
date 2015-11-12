# RESTACK

This tiny library helps you to write recursive functions without any ''stack overflow'' related pain.

Say you have a function like this:
```python
def factorial(value):
	return 1 if value == 1 else value * factorial(value-1)
```
It works fine until the ```value``` thing is less then a ```sys.getrecursionlimit()```.

RESTACK provides a solution (stolen from Dave Beazley, really)
```python
@restack.decorate
def factorial(value):
	return 1 if value == 1 else value * (yield {'value': value-1})
```

and then you can use it as a normal function:
``` python
>>> result = factorial(value=10000)  # note that keyword - like style is a mandatory
```

This decorated function is completely stack overflow free, because it doesn't use process's stack section at all.

Also stuff like this one is also possible (called maccarthy91 function):
```python
@restack.decorate
def maccarthy(value):
    if value > 100:
        return value - 10
    else:
        return (yield {'value': (yield {'value': value+11})})
```
##### So the rule is that: whenever you want to use a recursive call, just yield the dictionary, representing the function kwargs, that is it.