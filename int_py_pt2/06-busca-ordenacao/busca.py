class Busca:
    def busca_sequencial(lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return False

    def busca_binaria(self, lista, elemento):
        primeiro, ultimo = 0, (len(lista) - 1)

        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if lista[meio] == elemento:
                return meio
            else:
                if elemento < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return -1