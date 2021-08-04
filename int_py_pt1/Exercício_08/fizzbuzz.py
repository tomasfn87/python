def fizzbuzz(x):
    if x % 3 == 0 and x % 5 != 0:
        return 'Fizz'
    elif x % 3 != 0 and x % 5 == 0:
        return 'Buzz'
    elif x % 3 == 0 and x % 5 == 0:
        return 'FizzBuzz'
    else:
        return x
    
def test_fizzbuzz0():
    assert fizzbuzz(15) == 'FizzBuzz'

def test_fizzbuzz1():
    assert fizzbuzz(9) == 'Fizz'

def test_fizzbuzz2():
    assert fizzbuzz(10) == 'Buzz'

def test_fizzbuzz3():
    assert fizzbuzz(8) == 8

def test_fizzbuzz4():
    assert fizzbuzz(-1) == -1

def test_fizzbuzz5():
    assert fizzbuzz(0) == 'FizzBuzz'