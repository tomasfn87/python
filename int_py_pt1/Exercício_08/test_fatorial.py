def fatorial(x):
    if x < 0:
        return  0
    i = fat = 1
    while i <= x:
        fat = fat * i
        i += 1
    return fat

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial2():
    assert fatorial(2) == 2

def test_fatorial3():
    assert fatorial(3) == 6

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial5():
    assert fatorial(5) == 120

def test_fatorial_negativo():
    assert fatorial(-10) == 0

def main():
    print(fatorial(2))
main()

