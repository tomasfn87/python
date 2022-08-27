def vogal(e):
    if e in ('a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'):
        return True
    else:
        return False
        
    '''if c == 'a':
        return True
    elif c == 'e':
        return True
    elif c == 'i':
        return True
    elif c == 'o':
        return True
    elif c == 'u':
        return True
    elif c == 'A':
        return Truepy.
    elif c == 'E':
        return True
    elif c == 'I':
        return True
    elif c == 'O':
        return True
    elif c == 'U':
        return True
    else:
        return False'''

def test_vogal0():
    assert vogal('a') == True
def test_vogal1():
    assert vogal('b') == False
def test_vogal2():
    assert vogal('u') == True
def test_vogal3():
    assert vogal('Z') == False
def test_vogal4():
    assert vogal('A') == True