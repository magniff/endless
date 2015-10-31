def decorate(gen):

    def _wrapper(**kwargs):
        stack = [gen(**kwargs)]
        value = None
        while stack:
            try:
                value = stack[-1].send(value)
                stack.append(gen(**value))
                value = None
            except StopIteration as e:
                stack.pop()
                value = e.value
        return value

    return _wrapper
