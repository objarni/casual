import simplejson

def build_output(obj):
    pass

def selftest():
    with open('input.json') as f:
        content = f.read()
    movie = simplejson.loads(content)
    with open('result.txt') as f:
        expected = f.read()
    assert(build_output(movie) == expected)


if __name__ == '__main__':
    selftest()
