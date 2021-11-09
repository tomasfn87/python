import pymongo
import sys
sys.path.append("/home/morbi/filtering")
sys.path.append("/home/morbi/python/external/dict")
from texto import Texto as T
from listas import Listas as L

def criarListaProdutos(lista, ord=False, key="", inv=False):
    lista = list(lista)
    if len(lista) == 0:
        return False
    listaProdutos = []
    for i in range(0, len(lista)):
        listaProdutos.append({ "nome": "", "preco": 0 })
        listaProdutos[i]["nome"] = "{} {}".format(
            lista[i]["tipo"], lista[i]["subtipo"]
        )
        listaProdutos[i]["preco"] = lista[i]["preco"]
    if ord == True:
        return L.sortDictsByKey(listaProdutos, key, inv)
    return listaProdutos

def listarProdutos(lista, maiorItem):
    for i in lista:
        print(
            "{}{}|  R$ {}".format(
                i["nome"].capitalize(),
                T.espacar(maiorItem - len(i["nome"]) + 2),
                T.trocar_caracter(i["preco"], ".", ",")
            )
        )

def imprimirListaProdutos(separador, lista, ord=False, key="", inv=False):
    assert len(separador) == 1
    listaProdutos = criarListaProdutos(lista, ord, key, inv)
    if listaProdutos == False:
        return print("Nenhum resultado.")
    elif len(listaProdutos) == 1:
        print("1 resultado:")
    else:
        print("{} resultados:".format(len(listaProdutos)))
    maiorItem = L.analisarListaDict(listaProdutos, ["nome"])
    tamanhoSeparacao1 = maiorItem
    tamanhoSeparacao2 = L.analisarListaDict(listaProdutos, ["preco"])
    
    separacao1 = ""
    for i in range(0, tamanhoSeparacao1 + 2):
        separacao1 += separador
        i += 1
    
    separacao2 = ""
    for i in range(0, tamanhoSeparacao2 + 5):
        separacao2 += separador
        i += 1

    print("{} {}".format(separacao1, separacao2))
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
    print("Escolha uma das opções abaixo: ")
    print(" * Exibir todos, ordenados por:")
    print("   - Nome:  1) padrão     2) inverso") 
    print("   - Preço: 3) crescente  4) decrescente")
    print(" * Buscar por:")
    print("   - Tipo:  5) tipo       6) subtipo  7) ambos")
    print("   - Preço: 8) máximo     9) mínimo   0) ambos")
    print("\n* Digite uma das opções acima (s = sair): ", end="")

    busca = []

    opcao_1 = input()
    if opcao_1 == "1":
        busca = db.produtos.find({},{"_id":0}).sort("tipo", 1)
    elif opcao_1 == "2":
        busca = db.produtos.find({},{"_id":0}).sort("tipo", -1)
    elif opcao_1 == "3":
        busca = db.produtos.find({},{"_id":0}).sort("preco", 1)
    elif opcao_1 == "4":
        busca = db.produtos.find({},{"_id":0}).sort("preco", -1)
    elif opcao_1 == "5":
        opcao_tipo = input("Digite o tipo desejado: ")
        busca = db.produtos.find({"tipo": opcao_tipo.lower()},{"_id":0})\
                        .sort("subtipo", 1)
    elif opcao_1 == "6":
        opcao_subtipo = input("Digite o subtipo: ")
        busca = db.produtos.find(
            {"subtipo": opcao_subtipo.lower()},{"_id":0}
        ).sort("tipo", 1)
    elif opcao_1 == "7":
        opcao_2 = input("Digite o tipo ou subtipo: ")
        busca = db.produtos.find({"$or": [
            {"tipo": opcao_2.lower()},
            {"subtipo": opcao_2.lower()}
        ]},{"_id":0}).sort("tipo", 1)
    elif opcao_1 == "8":
        maximo = digitarNumero(
            "Digite o preço máximo: ",
            "Erro: o preço máximo deve ser inteiro ou decimal: "
        )
        busca = db.produtos.find({"preco": {"$lte": maximo}},{"_id":0})\
                        .sort("preco", -1)
    elif opcao_1 == "9":
        minimo = digitarNumero(
            "Digite o preço mínimo: ",
            "Erro: o preço mínimo deve ser inteiro ou decimal: "
        )
        busca = db.produtos.find({"preco": {"$gte": minimo}},{"_id":0})\
                        .sort("preco", 1)
    elif opcao_1 == "0":
        maximo = digitarNumero(
            "Digite o preço máximo: ",
            "Erro: o preço máximo deve ser inteiro ou decimal: "
        )
        minimo = digitarNumero(
            "Digite o preço mínimo: ",
            "Erro: o preço mínimo deve ser inteiro ou decimal: "
        )
        busca = db.produtos.find(
            {"preco": {"$lte": maximo, "$gte": minimo}},{"_id":0}\
        ).sort("preco", -1)
    elif opcao_1.lower() in ["s", "sair", "exit", "quit"]:
        return print("\nObrigado por consultar os produtos, até logo!")
    else:
        print("** ERRO! Opção inválida! **\n")
        return buscarProdutos(db)

    print()
    if opcao_1 in ["1", "4", "5", "6"]:
        imprimirListaProdutos("–", busca, 1, "nome")
    elif opcao_1 in ["2"]:
        imprimirListaProdutos("–", busca, 1, "nome", 1)
    else:
        imprimirListaProdutos("–", busca)
    print()
    return novaBusca(db)

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

with client:
    db = client.test

def main():
    print("Bem vindo à busca de produtos!", end=" ") 
    print("Vamos encontrar o que você precisa:\n")
    buscarProdutos(db)

if __name__ == "__main__":
    main()
