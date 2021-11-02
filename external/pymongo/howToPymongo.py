import pymongo
import sys
sys.path.append("/home/morbi/filtering")
from texto import Texto as T
            
def analisarListaDict(lista):
    maiorItem = 0
    tamanhoAtual = 0
    for i in lista:
        for key in i.keys():
            tamanhoAtual += len(str(i[key]))
        if tamanhoAtual > maiorItem:
            maiorItem = tamanhoAtual
        tamanhoAtual = 0
    return maiorItem

def criarListaProdutos(lista):
    lista = list(lista)
    listaProdutos = []
    for i in range(0, len(lista)):
        listaProdutos.append({ "nome": "", "preco": 0 })
        listaProdutos[i]["nome"] = "{} {}".format(
            lista[i]["tipo"], lista[i]["subtipo"]
        )
        listaProdutos[i]["preco"] = "{}".format(lista[i]["preco"])
    return listaProdutos

def listarProdutos(lista):
    listaProdutos = criarListaProdutos(lista)
    maiorItem = analisarListaDict(listaProdutos)
    for i in listaProdutos:
        print(
            "{}{}|  R$ {}".format(
                i["nome"].capitalize(),
                T.espacar(maiorItem - 2 - len(i["nome"])),
                T.trocar_caracter(i["preco"], ".", ",")
            )
        )

def imprimirListaProdutos(title, separator, lista, end=True):
    assert len(separator) == 1
    print(title)
    split = ""
    for i in range(0, len(title)):
        split += separator
        i += 1
    print(split)
    listarProdutos(lista)
    if end == True:
        print()

def novaBusca():
    print("Escolha uma das opções abaixo: ")
    print(" - 1) Nova busca")
    print(" - 0) Sair")
    print(" * Digite sua opção e aperte ENTER: ", end="")
    repetir = input()
    if repetir == "1":
        print()
        return buscarProdutos()
    elif repetir == "0":
        return print("\nSaindo... até a próxima busca!")
    else:
        print("** ERRO! Opção inválida! **\n")
        return novaBusca()

def buscarProdutos():
    print("Escolha uma das opções abaixo: ")
    print(" - 1) Ver todos os produtos ordenados por tipo")
    print(" - 2) Ver todos os produtos ordenados por preço (crescente)")
    print(" - 3) Ver todos os produtos ordenados por preço (decrescente)")
    print(" - 4) Buscar por tipo (Exemplo: 'laranja' ou 'pera')")
    print(" - 5) Buscar por subtipo (Exemplo: 'lima' ou 'red')")
    print(" - 6) Buscar por tipo ou subtipo")
    print(" - 7) Definir preço máximo")
    print(" - 8) Definir preço mínimo")
    print(" - 9) Definir preços máximo e mínimo")
    print(" - 0) Sair")
    print(" * Digite sua opção e aperte ENTER: ", end="")

    resultado = []

    opcao_1 = input()
    if opcao_1 == "1":
        resultado = db.produtos.find({},{"_id":0}).sort("tipo", 1)

    elif opcao_1 == "2":
        resultado = db.produtos.find({},{"_id":0}).sort("preco", 1)

    elif opcao_1 == "3":
        resultado = db.produtos.find({},{"_id":0}).sort("preco", -1)

    elif opcao_1 == "4":
        opcao_tipo = input("Digite o tipo desejado: ")
        resultado = db.produtos.find({"tipo": opcao_tipo},{"_id":0}) \
                        .sort("subtipo", 1)

    elif opcao_1 == "5":
        opcao_subtipo = input("Digite o subtipo: ")
        resultado = db.produtos.find({"subtipo": opcao_subtipo},{"_id":0}) \
                        .sort("tipo", 1)

    elif opcao_1 == "6":
        opcao_2 = input("Digite o tipo ou subtipo: ")
        resultado = db.produtos.find({"$or": [
            {"tipo": opcao_2},
            {"subtipo": opcao_2}
        ]}, {"_id":0}).sort("tipo", 1)

    elif opcao_1 == "7":
        maximo = float(input("Digite o preço máximo: "))
        resultado = db.produtos.find({"preco": {"$lte": maximo}},{"_id":0})\
                        .sort("preco", -1)

    elif opcao_1 == "8":
        minimo = float(input("Digite o preço mínimo: "))
        resultado = db.produtos.find({"preco": {"$gte": minimo}},{"_id":0})\
                        .sort("preco", 1)

    elif opcao_1 == "9":
        maximo = float(input("Digite o preço máximo: "))
        minimo = float(input("Digite o preço mínimo: "))
        resultado = db.produtos.find(
            {"preco": {"$lte": maximo, "$gte": minimo}},{"_id":0}\
        ).sort("preco", -1)

    elif opcao_1 == "0":
        return print("\nObrigado por consultar os produtos, até logo!")

    else:
        print("** ERRO! Opção inválida! **\n")
        return buscarProdutos()

    print()
    imprimirListaProdutos("Resultado da busca:", "-", resultado)
    novaBusca()

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

with client:
    db = client.test

def main():
    print("Bem vindo à busca de produtos! Vamos encontrar o que você precisa:\n")
    buscarProdutos()

main()
