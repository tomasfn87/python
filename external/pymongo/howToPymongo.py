import pymongo
import sys
sys.path.append("/home/morbi/filtering")
sys.path.append("/home/morbi/python/external/dict")
from texto import Texto as T
from listas import Listas as L

def criarListaProdutos(lista, ord=False, key="", inv=0):
    lista = list(lista)
    if len(lista) == 0:
        return False
    listaProdutos = []
    for i in range(0, len(lista)):
        listaProdutos.append({ "nome": "", "preco": 0 })
        listaProdutos[i]["nome"] = "{} {}".format(
            lista[i]["tipo"].capitalize(), lista[i]["subtipo"]
        )
        listaProdutos[i]["preco"] = lista[i]["preco"]
    if ord == True:
        return L.sortDictsByKey(listaProdutos, key, inv)
    return listaProdutos

def listarProdutos(lista, maiorItem):
    for i in lista:
        print(
            "{}{}|  R$ {}".format(
                i["nome"],
                T.espacar(maiorItem - len(i["nome"]) + 2),
                T.trocar_caracter(i["preco"], ".", ",")
            )
        )

def imprimirListaProdutos(separador, lista, ord=False, key="", inv=0):
    assert len(separador) == 1
    listaProdutos = criarListaProdutos(lista, ord, key, inv)

    if listaProdutos == False:
        return print("Nenhum resultado.")
    elif len(listaProdutos) == 1:
        print("1 resultado:")
    else:
        print("{} resultados:".format(len(listaProdutos)))

    maiorItem = L.analisarListaDict(listaProdutos, ["nome"])

    titulos = ["Nome", "Preço"]
    tamanhoSeparacao1 = maiorItem - len(titulos[0]) + 1
    tamanhoSeparacao2 = L.analisarListaDict(listaProdutos, ["preco"]) - len(titulos[1]) - 1
    
    separacao1 = "{} {}:".format(separador, titulos[0])
    for i in range(0, tamanhoSeparacao1 - 2):
        separacao1 += separador
        i += 1
    
    separacao2 = "{} {}:".format(separador, titulos[1])
    for i in range(0, tamanhoSeparacao2 + 5):
        separacao2 += separador
        i += 1

    print("{}|{}".format(separacao1, separacao2))
    listarProdutos(listaProdutos, maiorItem)

def novaBusca(db):
    print("Escolha uma das opções abaixo: ")
    print(" - 1) Nova busca  s) Sair")
    print(" * Digite sua opção e aperte ENTER: ", end="")
    repetir = input()
    if repetir == "1":
        print()
        return buscarProdutos(db)
    elif repetir.lower() in ["s", "sair", "exit", "quit"]:
        return print("\nSaindo... até a próxima busca!")
    else:
        print("** ERRO! Opção inválida! **\n")
        return novaBusca(db)

def digitarNumero(textoInput, textoErro):
    numero = T.verificar_numero(input(textoInput))
    while numero == False:
        numero = T.verificar_numero(input(textoErro))
    return numero

def buscarProdutos(db):
    print(
'''Escolha uma das opções abaixo (adicione 'i' para inverter [Ex: 34i])
    * Exibir todos, ordenados por:
                - 1) nome    - 2) preço
    * Buscar por:
      - Tipo:   - 3) tipo    - 4) subtipo  - 34) ambos
      - Preço:  - 5) máximo  - 6) mínimo   - 56) ambos'''
    )
    print("\n * Digite uma das opções acima (s): sair): ", end="")

    busca = []

    opcao_1 = input().lower()
    if opcao_1 == "1":
        busca = db.Produtos.find({},{"_id":0}).sort("tipo", 1)
    elif opcao_1 == "1i":
        busca = db.Produtos.find({},{"_id":0}).sort("tipo", -1)

    elif opcao_1 == "2":
        busca = db.Produtos.find({},{"_id":0}).sort("preco", 1)
    elif opcao_1 == "2i":
        busca = db.Produtos.find({},{"_id":0}).sort("preco", -1)

    elif opcao_1 in ["3", "3i"]:
        opcao_tipo = input("Digite o tipo desejado: ").lower()
        busca = db.Produtos.find({"tipo": opcao_tipo},{"_id":0})

    elif opcao_1 in ["4", "4i"]:
        opcao_subtipo = input("Digite o subtipo: ").lower()
        busca = db.Produtos.find({"subtipo": opcao_subtipo},{"_id":0})

    elif opcao_1 == "34":
        opcao_2 = input("Digite o tipo ou subtipo: ").lower()
        busca = db.Produtos.find({"$or": [
            {"tipo": opcao_2},
            {"subtipo": opcao_2}
        ]},{"_id":0})
    elif opcao_1 == "34i":
        opcao_2 = input("Digite o tipo ou subtipo: ").lower()
        busca = db.Produtos.find({"$or": [
            {"tipo": opcao_2},
            {"subtipo": opcao_2}
        ]},{"_id":0})

    elif opcao_1 in ["5", "5i"]:
        maximo = digitarNumero(
            "Digite o preço máximo: ",
            "Erro: o preço máximo deve ser inteiro ou decimal: "
        )
        if opcao_1 == "5":
            busca = db.Produtos.find({"preco": {"$lte": maximo}},{"_id":0})\
                        .sort("preco", 1)
        else:
            busca = db.Produtos.find({"preco": {"$lte": maximo}},{"_id":0})\
                        .sort("preco", -1)

    elif opcao_1 in ["6", "6i"]:
        minimo = digitarNumero(
            "Digite o preço mínimo: ",
            "Erro: o preço mínimo deve ser inteiro ou decimal: "
        )
        if opcao_1 == "6":
            busca = db.Produtos.find({"preco": {"$gte": minimo}},{"_id":0})\
                        .sort("preco", 1)
        else:
            busca = db.Produtos.find({"preco": {"$gte": minimo}},{"_id":0})\
                        .sort("preco", -1)

    elif opcao_1 in ["56", "56i"]:
        maximo = digitarNumero(
            "Digite o preço máximo: ",
            "Erro: o preço máximo deve ser inteiro ou decimal: "
        )
        minimo = digitarNumero(
            "Digite o preço mínimo: ",
            "Erro: o preço mínimo deve ser inteiro ou decimal: "
        )
        if opcao_1 == "56":
            busca = db.Produtos.find(
                {"preco": {"$lte": maximo, "$gte": minimo}},{"_id":0}\
            ).sort("preco", 1)
        else:
            busca = db.Produtos.find(
                {"preco": {"$lte": maximo, "$gte": minimo}},{"_id":0}\
            ).sort("preco", -1)

    elif opcao_1 in ["s", "sair", "exit", "quit"]:
        return print("\nObrigado por consultar os produtos, até logo!")
    else:
        print("** ERRO! Opção inválida! **\n")
        return buscarProdutos(db)

    print()
    # 1.1 ordem alfabética
    if opcao_1 in ["1", "3", "4", "34"]:
        imprimirListaProdutos("–", busca, 1, "nome")
    # 1.2 ordem alfabética inversa
    elif opcao_1.lower() in ["1i", "3i", "4i", "34i"]:
        imprimirListaProdutos("–", busca, 1, "nome", 1)
    # 2. demais casos (onde ordenação do mongodb basta)
    else:
        imprimirListaProdutos("–", busca)
    print()
    return novaBusca(db)


def main():
    try:
        pymongo.MongoClient(
            host = ["mongodb://127.0.0.1:27017"],
            serverSelectionTimeoutMS = 750
        ).server_info()
    except:
        print("ERROR: Connection to mongoDb refused.")
        return print("Please start mongodDb or enter correct host address.")

    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    with client:
        db = client.test

    print("Bem vindo à busca de produtos!", end=" ")
    print("Vamos encontrar o que você precisa:\n")
    buscarProdutos(db)

if __name__ == "__main__":
    main()