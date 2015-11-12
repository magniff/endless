import restack


def test_factorial():

    @restack.decorate
    def fac(n):
        return 1 if n == 1 else n * (yield {'n': n-1})

    assert fac(n=10) == 3628800
    assert fac(n=10000) == fac(n=9999) * 10000


def test_palindrome():

    # very unefficient recursive algorithm
    @restack.decorate
    def is_palindrome(word):
        return (
            len(word) in [0, 1] or word[0] == word[-1] and
            (yield {'word': word[1:-1]})
        )

    assert not is_palindrome(word='some arbitary text')
    assert is_palindrome(word='abcddcba')


# https://en.wikipedia.org/wiki/McCarthy_91_function
def test_maccarthy():

    @restack.decorate
    def maccarthy(value):
        if value > 100:
            return value - 10
        else:
            return (yield {'value': (yield {'value': value+11})})

    for value in range(-100, 100):
        assert maccarthy(value=value) == 91

    assert maccarthy(value=-1000000) == 91


# https://en.wikipedia.org/wiki/Ackermann_function
def test_ackermann():

    @restack.decorate
    def ackermann(m, n):
        if m == 0:
            return n + 1
        elif m > 0 and n == 0:
            return (yield {'m': m - 1, 'n': 1})
        elif m > 0 and n > 0:
            return (yield {'m': m - 1, 'n': (yield {'m': m, 'n': n-1})})

    assert ackermann(n=1, m=1) == 3
    assert ackermann(n=2, m=2) == 7
    assert ackermann(n=3, m=3) == 61
