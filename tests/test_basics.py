import restack


def test_factorial():

    @restack.decorate
    def fac(n):
        return 1 if n == 1 else n * (yield {'n': n-1})

    assert fac(n=10) == 3628800
    assert fac(n=10000) == fac(n=9999) * 10000


def test_palindrome():

    @restack.decorate
    def is_palindrome(word):
        return (
            len(word) in [0, 1] or word[0] == word[-1] and
            (yield {'word': word[1:-1]})
        )

    assert not is_palindrome(word='some arbitary text')
    assert is_palindrome(word='abcddcba')
