from inspect import signature
from functools import wraps


def endless(function):

    @wraps(function)
    def stackless_function_wrapper(*args, **kwargs):
        signature_instance = signature(function)

        def stackless_function(**kwargs):
            stack = [function(**kwargs)]
            value = None
            while stack:
                try:
                    value = stack[-1].send(value)
                    stack.append(function(**value))
                    value = None
                except StopIteration as e:
                    stack.pop()
                    value = e.value
            return value

        kwargs.update(signature_instance.bind_partial(*args).arguments)
        return stackless_function(**kwargs)

    return stackless_function_wrapper
