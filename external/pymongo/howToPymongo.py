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
    if ord:
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

    if not listaProdutos:
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
            numero = input(textoErro)
            if voltar(numero):
                return False
            numero = T.verificar_numero(numero)
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
    if opcao.lower() in ["v", "voltar"]:
        print()
        return True
    return False

def buscar(collection, query1, query2=False, sortBy=False, order=False):
    if not query2:
        termos = collection.find(query1)
    else:
        termos = collection.find(query1, query2)
    if sortBy and order:
        termos = termos.sort(sortBy, order)
    elif sortBy:
        termos = termos.sort(sortBy)
    return termos

def menuBusca(opcoes, mensagens, db):
    m, o, produtos, margem = mensagens, opcoes, db.Produtos, 13

    ## Declaração opções de Busca
    # Alfabética
    alf = o["ordem"]["alf"]
    alfTodos = alf["todos"]
    tipo = alf["tipo"]
    subtipo = alf["subtipo"]
    tipoAmbos = alf["tipoAmbos"]

    # Numérica
    num = o["ordem"]["num"]
    numTodos = num["todos"]
    precoMax = num["precoMax"]
    precoMin = num["precoMin"]
    precoAmbos = num["precoAmbos"]

    opcoesBusca = [
        alfTodos["normal"], alfTodos["inv"], tipo["normal"], tipo["inv"],
        subtipo["normal"], subtipo["inv"], tipoAmbos["normal"], 
        tipoAmbos["inv"], numTodos["normal"], numTodos["inv"], 
        precoMax["normal"], precoMax["inv"], precoMin["normal"],
        precoMin["inv"], precoAmbos["normal"], precoAmbos["inv"]
    ]

    # Menu principal
    print(m["menu"])
    print("{}{}".format(T.espacar(margem-3), m["comoInverter"]))
    print("{}{}".format(T.espacar(margem), m["selecionar"]), end="")

    busca, opcao_1 = [], input()

    ## Sair
    if opcao_1 in opcoes["sair"]:
        print("\n{}".format(m["tchau"]))
        return False

    # Opções de Busca
    elif opcao_1 in L.unirListas(opcoesBusca):
        ## Ordem alfabética
        # Todos
        if opcao_1 in L.unirListas([alfTodos["normal"], alfTodos["inv"]]):
            busca = buscar(produtos, {}, {"_id": 0})

        # Item 3 - Por tipo Ex: laranja, banana
        elif opcao_1 in L.unirListas([tipo["normal"], tipo["inv"]]):
            userInput = ("{}{}{}: ").format(
                T.espacar(margem), m["tipo"], m["voltar"]
            )
            opcao_tipo = input(userInput)
            if voltar(opcao_tipo):
                return menuBusca(o, m, db)
            busca = buscar(produtos, {"$or": [
                {"tipo": opcao_tipo.lower()}
            ]}, {"_id": 0})

        # Item 4 - Por subtipo Ex: lima, nanica
        elif opcao_1 in L.unirListas([subtipo["normal"], subtipo["inv"]]):
            userInput = ("{}{}{}: ").format(
                T.espacar(margem), m["subtipo"], m["voltar"]
            )
            opcao_subtipo = input(userInput)
            if voltar(opcao_subtipo):
                return menuBusca(o, m, db)
            busca = buscar(produtos, {"$or": [
                {"subtipo": opcao_subtipo.lower()},
                {"subtipo": opcao_subtipo.lower().capitalize()}
            ]}, {"_id": 0})

        # Item 34 - Por tipo e subtipo Ex: pera, maçã
        elif opcao_1 in L.unirListas([tipoAmbos["normal"], tipoAmbos["inv"]]):
            userInput = ("{}{}{}: ").format(
                T.espacar(margem), m["tipoSubtipo"], m["voltar"]
            )
            opcao_tipoAmbos = input(userInput)
            if voltar(opcao_tipoAmbos):
                return menuBusca(o, m, db)
            busca = buscar(produtos, {"$or": [
                {"tipo": opcao_tipoAmbos.lower()},
                {"subtipo": opcao_tipoAmbos.lower()},
                {"subtipo": opcao_tipoAmbos.lower().capitalize()}
            ]})

        ## Ordem numérica
        # Item 2 - todos, por preço
        elif opcao_1 in numTodos["normal"]:
            busca = buscar(produtos, {}, {"_id": 0}, "preco")
        elif opcao_1 in numTodos["inv"]:
            busca = buscar(produtos, {}, {"_id": 0}, "preco", -1)

        # Item 5 - definir preço máximo, por preço
        elif opcao_1 in L.unirListas([num["precoMax"]["normal"], num["precoMax"]["inv"]]):
            userInput = "{}{}{}: ".format(T.espacar(margem), m["precoMax"], m["voltar"])
            maximo = digitarNumero(userInput, m["precoMaxErr"])
            if not maximo:
                return menuBusca(o, m, db)
            if opcao_1 == "5":
                busca = buscar(produtos, {"preco": {"$lte": maximo}},\
                    {"_id": 0}, "preco")
            else:
                busca = buscar(produtos, {"preco": {"$lte": maximo}},\
                    {"_id": 0}, "preco", -1)

        # Item 6 - definir preço mínimo, por preço
        elif opcao_1 in L.unirListas([precoMin["normal"], precoMin["inv"]]):
            userInput = "{}{}{}: ".format(
                T.espacar(margem), m["precoMin"], m["voltar"]
            )
            minimo = digitarNumero(userInput, m["precoMinErr"])
            if not minimo:
                return menuBusca(o, m, db)
            if opcao_1 == precoMin["normal"]:
                busca = buscar(produtos, {"preco": {"$gte": minimo}},\
                            {"_id":0}, "preco")
            else:
                busca = buscar(produtos, {"preco": {"$gte": minimo}},\
                            {"_id":0}, "preco", -1)

        # Item 56 - Definir preços máximo e mínimo, por preço
        elif opcao_1 in L.unirListas([precoAmbos["normal"], precoAmbos["inv"]]):
            userInput = "{}{}{}: ".format(T.espacar(margem), m["precoMax"], m["voltar"])
            maximo = digitarNumero(userInput, m["precoMaxErr"])
            if not maximo:
                return menuBusca(o, m, db)
            userInput = "{}{}{}: ".format(T.espacar(margem), m["precoMin"], m["voltar"])
            minimo = digitarNumero(userInput, m["precoMinErr"])
            if not minimo:
                return menuBusca(o, m, db)
            if opcao_1 in precoAmbos["normal"]:
                busca = buscar(produtos,
                    {"preco": {"$lte": maximo, "$gte": minimo}},\
                        {"_id":0}, "preco")
            else:
                busca = buscar(produtos,
                    {"preco": {"$lte": maximo, "$gte": minimo}},\
                        {"_id":0}, "preco", -1)

        return (opcao_1, busca)

    else:
        ## Opção inválida
        print("{}\n".format(m["opcaoInvalida"]))

    return menuBusca(opcoes, m, db)

def buscarProdutos(db):
    opcoes = {
        "sair": ["s", "sair", "exit", "quit", "-"],
        "ordem": {
            "alf": {
                "todos": {
                    "normal": ["1"],
                    "inv": ["-1", "1-"]
                },
                "tipo": {
                    "normal": ["3"],
                    "inv": ["-3", "3-"]
                },
                "subtipo": {
                    "normal": ["4"],
                    "inv": ["-4", "4-"]
                },
                "tipoAmbos": {
                    "normal": ["34", "43"],
                    "inv": ["-34", "34-", "3-4", "-43", "43-", "4-3"]
                }
            },
            "num": {
                "todos": {
                    "normal": ["2"],
                    "inv": ["-2", "2-"]
                },
                "precoMax": {
                    "normal": ["5"],
                    "inv": ["-5", "5-"]
                },
                "precoMin": {
                    "normal": ["6"],
                    "inv": ["-6", "6-"]
                },
                "precoAmbos": {
                    "normal": ["56", "65"],
                    "inv": ["-56", "56-", "5-6", "-65", "65-", "6-5"]
                }
            }
        }
    }

    mensagens = {
        "menu":
'''\
                                            .:.:.:.                     :.:.:*:.:.:.:.:.:.*.:.:
                                              :. :.___               :.:*:.:.:.:*:.:.*.:.:.:.:.*.:
         __________________________________________|_|__________    :*:.:.*.:.\\.:.| :/:*/:.:*:.:.:
      ./:/:/:/:/:/:/:/:/:/:/:   Bem vinda à   :\:\:\:\:\:\:\:\:\:\.  :.:*\\.:.\\*:\||.|.:|:/.:*:.:
    ./:/:/:/:/:/:/:/:/:/:/:/:  Casa da Busca  :\:\:\:\:\:\:\:\:\:\:\. *.:.:\\:\\\\:.||/.:.|.*|.:*:
  ./:/:/:/:/:/:/:/:/:/:/:/:|:|:|:|:|:|:|:|:|:|:|:\:\:\:\:\:\:\:\:\:\:\. .:\\_\\\\*:.|| :.//:/:*:.
 =======================================================================     \\\\  ||  //
        |     Exibir     |               Buscar                |               \\\\| |//
        |...... .........|....... .................. ..........|                \   /
        |      Todos     |       Tipo       :       Preço      |                 | |
        |.... ...........|... ..............:... ..............|                 | |
        |    1. nome     |    3. tipo       :    5. máximo     |                 | | 
        |    2. preço    |    4. subtipo    :    6. mínimo     |                 | |    \|    |
/|/     |                |   34. ambos      :   56. ambos      |         \       | |     |  \/
/| /____|                |                  :                  |_________\\\\|____/   \____\__|_______
''',

        "comoInverter": "(adicione '-' -> ordem inversa  Ex: -2, -43, 5-6 ou 65-)",
        "selecionar": "* Digite uma das opções acima ou [S]air: ",
        "voltar": " (ou [V]oltar)", 
        "tchau": "Obrigado por consultar os produtos, até logo!",
        #inputs {
        "tipo": "* Digite o tipo",
        "subtipo": "* Digite o subtipo",
        "tipoSubtipo": "* Digite o tipo ou subtipo",
        "precoMin": "* Digite o preço mínimo",
        "precoMinErr": "Erro: o preço mínimo deve ser inteiro ou decimal: ",
        "precoMax": "* Digite o preço máximo",
        "precoMaxErr": "Erro: o preço máximo deve ser inteiro ou decimal: ",
        "precoMaxMinErr": "Erro: o preço mínimo tem que ser menor que o preço máximo: ",
        # }
        "opcaoInvalida": "** ERRO! Opção inválida! **"
    }

    termosBusca = menuBusca(opcoes, mensagens, db)
    if not termosBusca:
        return

    opcao = termosBusca[0]
    busca = termosBusca[1]

    print()

    alf = opcoes["ordem"]["alf"]

    alfabeticaNormal = [
        alf["todos"]["normal"],
        alf["tipo"]["normal"],
        alf["subtipo"]["normal"],
        alf["tipoAmbos"]["normal"]
    ]

    alfabeticaInversa = [
        alf["todos"]["inv"],
        alf["tipo"]["inv"],
        alf["subtipo"]["inv"],
        alf["tipoAmbos"]["inv"]
    ]

    # 1 Ordem alfabética
    if opcao in L.unirListas(alfabeticaNormal):
        imprimirListaProdutos("–", busca, 1, "nome")
    # 2 Ordem alfabética inversa
    elif opcao.lower() in L.unirListas(alfabeticaInversa):
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
        buscarProdutos(db)
    else:
        return

if __name__ == "__main__":
    main()
