from inspect import signature
from functools import wraps


# 10000 should be enough for everyone, you know
MAX_DEPTH = 10000
ERROR_TEMPLATE = (
    "Function {fname} exhausted virtual call stack. Tip: Examine this function"
    " and enlarge MAX_DEPTH (current {depth}) variable if needed."
)


def make(function):

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
                    if len(stack) > MAX_DEPTH:
                        raise RuntimeError(
                            ERROR_TEMPLATE.format(
                                fname=function.__name__, depth=MAX_DEPTH
                            )
                        )
                    value = None
                except StopIteration as result_handler:
                    stack.pop()
                    value = result_handler.value
            return value

        kwargs.update(signature_instance.bind_partial(*args).arguments)
        return stackless_function(**kwargs)

    return stackless_function_wrapper
