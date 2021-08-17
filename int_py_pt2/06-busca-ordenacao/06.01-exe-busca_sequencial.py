def busca_sequencial(seq, x):
    # (list, float) -> bool
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False

'''É um metodo bastante ineficaz, pois procura um a um pelos elementos
de uma lista. Funciona apensar com um volume pequeno de dados.

Tem alta complexidade computacional, o que faz com que torne-se
lenta quando o volume de dados é grande. Diz-se que é um
algorismo ineficiente.'''