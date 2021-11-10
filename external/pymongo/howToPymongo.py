import pymongo
import sys
sys.path.append("/home/morbi/filtering")
sys.path.append("/home/morbi/python/external/dict")
from texto import Texto as T
from listas import Listas as L

def verificarBusca(mongoURL):
    while not verificarMongo(mongoURL, 1500):
        return reconectar(mongoURL)
    return True

def verificarMongo(mongoURL, timeout):
    try:
        pymongo.MongoClient(
            host = [mongoURL], serverSelectionTimeoutMS = timeout
        ).server_info()
        return True
    except:
        print("ERRO: Conexão ao mongoDb recusada.")
        print("Por favor inicie o mongodDb ou verifique o endereço do MongoClient.")
        print("Tentar novamente?", end=" ")
        return False

def reconectar(mongoURL):
    retry = input().lower()
    if retry in ["s",  "sim", "y", "yes"]:
        return verificarBusca(mongoURL)
    elif retry in ["n", "não", "nao", "no", "non", "nein"]:
        print("A busca funciona em um banco de dados cujos itens possuem as chaves 'tipo', 'subtipo' e 'preco'. Configure o seu mongoDb e tente novamente.")
        return False
    else:
        print("Opção inválida, digite [S]im ou [N]ão:", end=" ")
        reconectar(mongoURL)

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

def listarProdutos(lista, maiorItem, larguraMinimaCol1):
    for i in lista:
        if maiorItem < larguraMinimaCol1:
            print(
                "{}{}|  R$ {}".format(
                    i["nome"],
                    T.espacar(larguraMinimaCol1 - len(i["nome"]) + 3),
                    T.trocar_caracter(i["preco"], ".", ",")
                )
            )
        else:
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
    else:
        print("Itens encontrados: {}\n".format(len(listaProdutos)))

    maiorItem1 = L.analisarListaDict(listaProdutos, ["nome"])
    maiorItem2 = L.analisarListaDict(listaProdutos, ["preco"])

    titulos = ["Nome", "Preço"]
    
    tamanhoSeparacao1 = maiorItem1 - len(titulos[0]) + 1
    tamanhoSeparacao2 = maiorItem2 - len(titulos[1]) - 3
    
    separacao1 = "{} {} ".format(separador, titulos[0])
    for i in range(0, tamanhoSeparacao1 - 2):
        separacao1 += separador
        i += 1
    
    separacao2 = "{}{}{} {} ".format(
        separador, separador, separador, titulos[1]
    )
    for i in range(0, tamanhoSeparacao2 + 5):
        separacao2 += separador
        i += 1

    print("{}|{}".format(separacao1, separacao2))

    larguraMinimaCol1 = len(titulos[0])

    listarProdutos(listaProdutos, maiorItem1, larguraMinimaCol1)
    
def digitarNumero(textoInput, textoErro):
    numero = input(textoInput)
    if voltar(numero):
        numero = False
    else:
        numero = T.verificar_numero(numero)
        while not numero:
            numero = T.verificar_numero(input(textoErro))
    return numero

def novaBusca(db):
    print("Escolha uma das opções abaixo: ")
    print(" - 1) Nova busca  [S]air")
    print(" * Digite sua opção e aperte ENTER: ", end="")
    repetir = input()
    if repetir == "1":
        print()
        return buscarProdutos(db)
    elif repetir.lower() in ["s", "sair", "exit", "quit", "-"]:
        return print("\nSaindo... até a próxima busca!")
    else:
        print("** ERRO! Opção inválida! **\n")
        return novaBusca(db)

def voltar(opcao):
    if str(opcao).lower() in ["v", "voltar"]:
        print()
        return True
    return False
    
def menuBusca(opcoes, db):
    print(
'''Escolha uma das opções abaixo (adicione '-' para inverter [Ex: -34])
    * Exibir todos, ordenados por:
                - 1) nome    - 2) preço
    * Buscar por:
      - Tipo:   - 3) tipo    - 4) subtipo  - 34) ambos
      - Preço:  - 5) máximo  - 6) mínimo   - 56) ambos'''
    )
    print("\n * Digite uma das opções acima ou [S]air: ", end="")

    busca = []
    opcao_1 = input()

    for i in opcoes:
        if opcao_1 in i:
            ## Sair
            if opcao_1 in opcoes[0]:
                print("\nObrigado por consultar os produtos, até logo!")
                return False

            ## Ordem alfabética
            elif opcao_1 in opcoes[1] or opcao_1 in opcoes[2]:
                # Item 1 - Todos, por nome
                if opcao_1 == "1":
                    busca = db.Produtos.find({},{"_id":0}).sort("tipo", 1)
                elif opcao_1 == "-1":
                    busca = db.Produtos.find({},{"_id":0}).sort("tipo", -1)
                # Item 3 - Por tipo Ex: laranja, banana
                elif opcao_1 in ["3", "-3"]:
                    opcao_tipo = input(" * Digite o tipo (ou [V]oltar): ")
                    if voltar(opcao_tipo):
                        return menuBusca(opcoes, db)
                    busca = db.Produtos.find({"$or": [
                        {"tipo": opcao_tipo.lower()}
                    ]}, {"_id":0})
                # Item 4 - Por subtipo Ex: lima, nanica
                elif opcao_1 in ["4", "-4"]:
                    opcao_subtipo = input(" * Digite o subtipo (ou [V]oltar): ")
                    if voltar(opcao_subtipo):
                        return menuBusca(opcoes, db)
                    busca = db.Produtos.find({"$or": [
                        {"subtipo": opcao_subtipo.lower()},
                        {"subtipo": opcao_subtipo.lower().capitalize()}
                    ]}, {"_id":0})
                # Item 34 - Por tipo e subtipo Ex: pera, verde
                elif opcao_1 in ["34", "-34"]:
                    opcao_2 = input(" * Digite o tipo ou subtipo (ou [V]oltar): ")
                    if voltar(opcao_2):
                        return menuBusca(opcoes, db)
                    busca = db.Produtos.find({"$or": [
                        {"tipo": opcao_2.lower()},
                        {"subtipo": opcao_2.lower()},
                        {"subtipo": opcao_2.lower().capitalize()}
                    ]}, {"_id":0})
                return (opcao_1, busca)

            ## Ordem numérica
            elif opcao_1 in opcoes[3]:
                # Item 2 - todos, por preço
                if opcao_1 == "2":
                    busca = db.Produtos.find({},{"_id":0}).sort("preco", 1)
                elif opcao_1 == "-2":
                    busca = db.Produtos.find({},{"_id":0}).sort("preco", -1)
                # Item 5 - definir preço máximo, por preço
                elif opcao_1 in ["5", "-5"]:
                    userInput = " * Digite o preço máximo (ou [V]oltar): "
                    error = "Erro: o preço máximo deve ser inteiro ou decimal: "
                    maximo = digitarNumero(userInput, error)
                    if not maximo:
                        return menuBusca(opcoes, db)
                    if opcao_1 == "5":
                        busca = db.Produtos.find({"preco": {"$lte": maximo}},{"_id":0})\
                                    .sort("preco", 1)
                    else:
                        busca = db.Produtos.find({"preco": {"$lte": maximo}},{"_id":0})\
                                    .sort("preco", -1)
                # Item 6 - definir preço mínimo, por preço
                elif opcao_1 in ["6", "-6"]:
                    userInput = " * Digite o preço mínimo (ou [V]oltar): "
                    error = "Erro: o preço mínimo deve ser inteiro ou decimal: "
                    minimo = digitarNumero(userInput, error)
                    if not minimo:
                        return menuBusca(opcoes, db)
                    if opcao_1 == "6":
                        busca = db.Produtos.find({"preco": {"$gte": minimo}},{"_id":0})\
                                    .sort("preco", 1)
                    else:
                        busca = db.Produtos.find({"preco": {"$gte": minimo}},{"_id":0})\
                                    .sort("preco", -1)
                # Item 56 - Definir preços máximo e mínimo, por preço
                elif opcao_1 in ["56", "-56"]:
                    userInput = " * Digite o preço máximo (ou [V]oltar): "
                    error = "Erro: o preço máximo deve ser inteiro ou decimal: "
                    maximo = digitarNumero(userInput, error)
                    if not maximo:
                        return menuBusca(opcoes, db)
                    userInput = " * Digite o preço mínimo (ou [V]oltar): "
                    error = "Erro: o preço mínimo deve ser inteiro ou decimal: "
                    minimo = digitarNumero(userInput, error)
                    if not minimo:
                        return menuBusca(opcoes, db)
                    if opcao_1 == "56":
                        busca = db.Produtos.find(
                            {"preco": {"$lte": maximo, "$gte": minimo}},{"_id":0}\
                        ).sort("preco", 1)
                    else:
                        busca = db.Produtos.find(
                            {"preco": {"$lte": maximo, "$gte": minimo}},{"_id":0}\
                        ).sort("preco", -1)
                return (opcao_1, busca)
    ## Opção inválida
    print("** ERRO! Opção inválida! **\n")
    return menuBusca(opcoes, db)
    
def buscarProdutos(db):
    opcoes = [
        # 0 Sair
        ["s", "sair", "exit", "quit", "-"],
        # 1 Ordem alfabética
        ["1", "3", "4", "34"],
        # 2 Ordem alfabética inversa
        ["-1", "-3", "-4", "-34"],
        # 3 Input numérico
        ["2", "-2", "5", "-5", "6", "-6", "56", "-56"]
    ]

    termosBusca = menuBusca(opcoes, db)
    if not termosBusca:
        return
    
    opcao = termosBusca[0]
    busca = termosBusca[1]

    print()
    # 1 Ordem alfabética
    if opcao in opcoes[1]:
        imprimirListaProdutos("–", busca, 1, "nome")
    # 2 Ordem alfabética inversa
    elif opcao.lower() in opcoes[2]:
        imprimirListaProdutos("–", busca, 1, "nome", 1)
    # * Demais casos: mongoDb já traz ordenado
    else:
        imprimirListaProdutos("–", busca)
    print()
    novaBusca(db)

def main():
    mongoURL = "mongodb://127.0.0.1:27017"

    if verificarBusca(mongoURL):
        client = pymongo.MongoClient(mongoURL)
        with client:
            db = client.test

        print("Bem vindo à busca de produtos!", end=" ")
        print("Vamos encontrar o que você precisa:\n")
        buscarProdutos(db)
    else:
        return

if __name__ == "__main__":
    main()
