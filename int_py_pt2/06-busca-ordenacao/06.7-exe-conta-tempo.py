import ordenar
import aleatorio
import time

class ContaTempo:
    def comparar(self, funcao_algoritmo, lista, str_algoritmo):
        t = time.time
        before = t()
        funcao_algoritmo(lista)
        after = t()
        print("\t" + str_algoritmo, "Sort took", "{0:.5f}".format(after - before), "seconds.")

    def compara(self, n):
        C = ContaTempo()
        compare = C.comparar
        
        listaA = aleatorio.lista_aleatoria(n)
        listaB = aleatorio.lista_quase_ordenada(n)

        o = ordenar.Ordenar()

        print("Random list {")
        compare(o.selecao_direta, listaA[:], "Direct Selection")
        compare(o.bolha,          listaA[:], "Bubble")
        compare(o.bolha_curta,    listaA[:], "Short Bubble")
        compare(o.insertion,      listaA[:], "Insertion")
        print("}\n\nAlmost ordered list {")
        compare(o.selecao_direta, listaB[:], "Direct Selection")
        compare(o.bolha,          listaB[:], "Bubble")
        compare(o.bolha_curta,    listaB[:], "Short Bubble")
        compare(o.insertion,      listaB[:], "Insertion")
        print("}")

def comparar():
    ct = ContaTempo()
    comp = ct.compara
    while True:
        n = int(input("Insira o número de itens das listas a serem testadas (-1 para sair): "))
        if n == -1:
            return
        else:
            print("\nTestando algoritmos de busca com listas de", n, "itens: \n")
            comp(n)
comparar()
