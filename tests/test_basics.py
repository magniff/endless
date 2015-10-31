import restack


def test_factorial():

    @restack.decorate
    def fac(n):
        return 1 if n == 1 else n * (yield {'n': n-1})

    assert fac(n=10) == 3628800
    assert fac(n=10000) == fac(n=9999) * 10000
