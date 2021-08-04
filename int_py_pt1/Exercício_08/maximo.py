def maximo(x, y):
    if x < y:
        return y
    elif x == y:
        return x
    else:
        return x

def test_maximo0():
    assert maximo(2, 1) == 2

def test_maximo1():
    assert maximo(3, 2) == 3

def test_maximo2():
    assert maximo(-2, -1) == -1

def test_maximo_same():
    assert maximo(1, 1) == 1