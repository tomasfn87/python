def primo(n):
    if n <= 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    else:
        div = 2
        while n > div and n % div != 0:
            div += 1
        if n == div:
            return True
        elif n % div == 0:
            return False
'''
    Usei um método diferente para calcular o número primo. O número-chave é 2, pois o 
número deve ser dividido a partir de 3, pois o número 2 é único número par que também
é primo. Portanto, a divisão será usada para verificar se o número é primo somente 
após n>2. Para os valores de n (0, 1, 2), uma regra if definirá o resultado.  A 
varíavel 'div' armazena o número que vai ser progressivamente usado como dividendo 
para verificar se o número é primo, começando por 2, 2+1, 2+1+1, etc.
'''
def maior_primo(m):
    while primo(m) == False:
        m -= 1
    return m
'''
    Aqui basta subtrair um algarismo do valor m especificado até encontrar o 
próximo número primo abaixo (por isso a subtração '    m -= 1'). O valor será devolvido
em '    return m' para o usuário, assim que m assumir um valor de número primo, quando
'primo(m) == True', interrompendo o loop 'while' e rodando os comandos na mesma 
indentação (apenas '    return m' nesse caso).
'''
def test_primo0():
    assert primo(701) == True
def test_primo1():
    assert primo(3) == True
def test_primo2():
    assert primo(13) == True
def test_primo3():
    assert primo(1) == False
def test_primo4():
    assert primo(0) == False
def test_primo5():
    assert primo(9) == False
def test_primo6():
    assert primo(40) == False
def test_primo7():
    assert primo(373) == True

def test_maior_primo0():
    assert maior_primo(12) == 11
def test_maior_primo1():
    assert maior_primo(102) == 101
def test_maior_primo2():
    assert maior_primo(4) == 3
def test_maior_primo3():
    assert maior_primo(759) == 757
def test_maior_primo4():
    assert maior_primo(765) == 761