import pymongo
import sys
sys.path.append('/home/morbi/filtering')
from texto import Texto as T

def listarProdutos(lista):
    for i in range(0, len(lista)):
        print(
            "{} {}\t | R${}".format(
            lista[i]["tipo"].capitalize(),
            lista[i]["subtipo"],
            T.trocar_caracter(lista[i]["preco"], ".", ",")
        ))

def imprimirListaProdutos( title, arr, separator, end=True):
    assert len(separator) == 1
    print(title)
    split = ""
    for i in range(0, len(title)):
        split += separator
        i += 1
    print(split)
    listarProdutos(list(arr))
    if end == True:
        print()

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

with client:
    db = client.test
    porNome = db.produtos.find().sort("tipo", 1)
    porPreco = db.produtos.find().sort("preco", -1)
    porPrecoMaiorOuIgual5 = db.produtos.find({"preco": {"$gte": 5}}).sort("preco", 1)
    porPrecoMenorOuIgual6 = db.produtos.find({"preco": {"$lte": 6}}).sort("preco", -1)
    porPrecoMaior4Menor7 = db.produtos.find({"preco": {"$gt": 4, "$lt": 7}}).sort("preco", 1)

"""
imprimirListaProdutos("Por nome (crescente)", porNome, "-")
imprimirListaProdutos("Por preco (descrescente)", porPreco, "-")
imprimirListaProdutos("Por preco: maior ou igual a 5 (crescente)", porPrecoMaiorOuIgual5, "-")
imprimirListaProdutos("Por preco: menor ou igual a 6 (decrescente)", porPrecoMenorOuIgual6, "-")
imprimirListaProdutos("Por preço: maior que 4 e menor que 7 (crescente)", porPrecoMaior4Menor7, "-", False)
"""

def buscarProdutos():
    print("Escolha uma das opções abaixo: ")
    print(" - 1) para ver todos os produtos")
    print(" - 2) para buscar por tipo \n   - Exemplo: 'laranja' ou 'pera'")
    print(" - 3) para buscar por subtipo \n   - Exemplo: 'lima' ou 'red'")
    print("\nDigite sua opção e aperte ENTER (0 para sair): ", end="")

    resultado = []

    opcao_1 = input()
    if opcao_1 == "1":
        resultado = db.produtos.find({},{"_id":0}).sort("tipo", 1)
    elif opcao_1 == "2":
        opcao_tipo = input("Digite o tipo desejado: ")
        resultado = db.produtos.find({"tipo": opcao_tipo},{"_id":0}).sort("subtipo", 1)
    elif opcao_1 == "3":
        opcao_subtipo = input("Digite o subtipo: ")
        resultado = db.produtos.find({"subtipo": opcao_subtipo},{"_id":0}).sort("tipo", 1)
    elif opcao_1 == "0":
        return
    else:
        print("** ERRO! Opção inválida! **")
        return buscarProdutos()
    imprimirListaProdutos("\nResultado da busca:", resultado, "-")
    return buscarProdutos()


def main():
    print("Bem vindo à busca de produtos! Vamos encontrar o que você precisa:\n")
    buscarProdutos()

main()