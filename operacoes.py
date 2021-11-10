class Operacoes:
    def mais(A, B):
        return A + B
    def menos(A, B):
        return A - B
    def vezes(A, B):
        return A * B
    def dividir(A, B):
        return A // B

def main():
    op = Operacoes
    print(
        op.mais(2, 3), op.menos(3, 2), 
        op.vezes(4, 2), op.dividir(12, 2)
    )

main()