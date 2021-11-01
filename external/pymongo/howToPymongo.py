import pymongo
import sys
sys.path.append("/home/morbi/filtering")
from texto import Texto as T

def espacar(n):
    espaco = ""
    while len(espaco) < n:
        espaco += " "
    return espaco
            
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

def listarProdutos(lista):
    listaProdutos = criarListaProdutos(lista)
    maiorItem = analisarListaDict(listaProdutos)
    for i in listaProdutos:
        print(
            "{}{}|  R${}".format(
                i["nome"].capitalize(),
                espacar(maiorItem - 2 - len(i["nome"])),
                T.trocar_caracter(i["preco"], ".", ",")
            )
        )

def imprimirListaProdutos(title, lista, separator, end=True):
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

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

with client:
    db = client.test
    # porNome = db.produtos.find().sort("tipo", 1)
    # porPreco = db.produtos.find().sort("preco", -1)
    # porPrecoMaiorOuIgual5 = db.produtos.find({"preco": {"$gte": 5}}).sort("preco", 1)
    # porPrecoMenorOuIgual6 = db.produtos.find({"preco": {"$lte": 6}}).sort("preco", -1)
    # porPrecoMaior4Menor7 = db.produtos.find({"preco": {"$gt": 4, "$lt": 7}}).sort("preco", 1)

"""
imprimirListaProdutos("Por nome (crescente)", porNome, "-")
imprimirListaProdutos("Por preco (descrescente)", porPreco, "-")
imprimirListaProdutos("Por preco: maior ou igual a 5 (crescente)", porPrecoMaiorOuIgual5, "-")
imprimirListaProdutos("Por preco: menor ou igual a 6 (decrescente)", porPrecoMenorOuIgual6, "-")
imprimirListaProdutos("Por preço: maior que 4 e menor que 7 (crescente)", porPrecoMaior4Menor7, "-", False)
"""

def buscarProdutos():
    print("Escolha uma das opções abaixo: ")
    print(" - 1) para ver todos os produtos ordenados por tipo")
    print(" - 2) para ver todos os produtos ordenados por preço (crescente)")
    print(" - 3) para ver todos os produtos ordenados por preço (decrescente)")
    print(" - 4) para buscar por tipo (Exemplo: 'laranja' ou 'pera')")
    print(" - 5) para buscar por subtipo (Exemplo: 'lima' ou 'red')")
    print(" - 6) para buscar por tipo ou subtipo")
    print("\nDigite sua opção e aperte ENTER (0 para sair): ", end="")

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
        resultado = db.produtos.find({"tipo": opcao_tipo},{"_id":0}).sort("subtipo", 1)
    elif opcao_1 == "5":
        opcao_subtipo = input("Digite o subtipo: ")
        resultado = db.produtos.find({"subtipo": opcao_subtipo},{"_id":0}).sort("tipo", 1)
    elif opcao_1 == "6":
        opcao_2 = input("Digite o tipo ou subtipo: ")
        resultado = db.produtos.find({"$or": [{"tipo": opcao_2}, {"subtipo": opcao_2}]},{"_id":0}).sort("tipo", 1)
    elif opcao_1 == "0":
        return
    else:
        print("** ERRO! Opção inválida! **")
        return buscarProdutos()
    print()
    imprimirListaProdutos("Resultado da busca:", resultado, "-")
    return buscarProdutos()

def main():
    print("Bem vindo à busca de produtos! Vamos encontrar o que você precisa:\n")
    buscarProdutos()

main()
# imprimirListaProdutos("Lista de produtos", porNome, "-", False)

