import pymongo
import sys
sys.path.append("/home/morbi/filtering")
sys.path.append("/home/morbi/python/external/dict")
from texto import Texto as T
from listas import Listas as L

class Dados:
    def __init__(self, mongoURL):
        self.URL = mongoURL

    def verificarBusca(self):
        while not Dados.verificarMongo(self, 1500):
            return Dados.reconectar(self)
        return True

    def verificarMongo(self, timeout):
        try:
            pymongo.MongoClient(
                host = [self.URL], serverSelectionTimeoutMS = timeout
            ).server_info()
            return True
        except:
            print("ERRO: Conexão ao mongoDb recusada.")
            print("Por favor inicie o mongodDb ou verifique o endereço do MongoClient.")
            print("Tentar novamente?", end=" ")
            return False

    def reconectar(self):
        retry = input().lower()
        if retry in ["s",  "sim", "y", "yes"]:
            return Dados.verificarBusca(self)
        elif retry in ["n", "não", "nao", "no", "non", "nein"]:
            print("A busca funciona em um banco de dados cujos itens", end=" ")
            print("possuem as chaves 'tipo', 'subtipo' e 'preco'.")
            print("Configure o seu mongoDb e tente novamente.")
            return False
        else:
            print("Opção inválida, digite [S]im ou [N]ão:", end=" ")
            Dados.reconectar(self)

class Busca:
    def __init__(self, db):
        self.db = db

    def digitarNumero(textoInput, textoErro):
        numero = input(textoInput)
        if Busca.voltar(numero):
            numero = False
        else:
            numero = T.verificar_numero(numero)
            while not numero:
                numero = input(textoErro)
                if Busca.voltar(numero):
                    return False
                numero = T.verificar_numero(numero)
        return numero

    def voltar(opcao):
        if opcao.lower() in ["v", "voltar"]:
            print()
            return True
        return False

    def novaBusca(self):
        print("Escolha uma das opções abaixo: ")
        print(" - 1) Nova busca  [S]air")
        print(" * Digite sua opção e aperte ENTER: ", end="")
        repetir = input()
        if repetir == "1":
            print()
            return Busca.buscarProdutos(self)
        elif repetir.lower() in ["s", "sair", "exit", "quit", "-"]:
            return print("\nSaindo... até a próxima busca!")
        else:
            print("** ERRO! Opção inválida! **\n")
            return Busca.novaBusca(self)

    def menuBusca(self, opcoes, mensagens):
        o, m, produtos, margem = opcoes, mensagens, self.db.Produtos, 13

        ## Declaração opções de Busca
        # Alfabética
        alf = o["ordem"]["alf"]
        alfTodos, tipo = alf["todos"], alf["tipo"]
        subtipo, tipoAmbos = alf["subtipo"], alf["tipoAmbos"]

        # Numérica
        num = o["ordem"]["num"]
        numTodos, precoMax = num["todos"], num["precoMax"]
        precoMin, precoAmbos = num["precoMin"], num["precoAmbos"]

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
            if opcao_1 in L.unirListas([alfTodos["normal"],\
                alfTodos["inv"]]):
                busca = Busca.buscar(produtos, {}, {"_id": 0})

            # Item 3 - Por tipo Ex: laranja, banana
            elif opcao_1 in L.unirListas([tipo["normal"], tipo["inv"]]):
                userInput = ("{}{}{}: ").format(
                    T.espacar(margem), m["tipo"], m["voltar"]
                )
                opcao_tipo = input(userInput)
                if Busca.voltar(opcao_tipo):
                    return Busca.menuBusca(self, o, m)
                busca = Busca.buscar(produtos, {"$or": [
                    {"tipo": opcao_tipo.lower()}
                ]}, {"_id": 0})

            # Item 4 - Por subtipo Ex: lima, nanica
            elif opcao_1 in L.unirListas([subtipo["normal"],\
                subtipo["inv"]]):
                userInput = ("{}{}{}: ").format(
                    T.espacar(margem), m["subtipo"], m["voltar"]
                )
                opcao_subtipo = input(userInput)
                if Busca.voltar(opcao_subtipo):
                    return Busca.menuBusca(self, o, m)
                busca = Busca.buscar(produtos, {"$or": [
                    {"subtipo": opcao_subtipo.lower()},
                    {"subtipo": opcao_subtipo.lower().capitalize()}
                ]}, {"_id": 0})

            # Item 34 - Por tipo e subtipo Ex: pera, maçã
            elif opcao_1 in L.unirListas([tipoAmbos["normal"],\
                tipoAmbos["inv"]]):
                userInput = ("{}{}{}: ").format(
                    T.espacar(margem), m["tipoSubtipo"], m["voltar"]
                )
                opcao_tipoAmbos = input(userInput)
                if Busca.voltar(opcao_tipoAmbos):
                    return Busca.menuBusca(self, o, m)
                busca = Busca.buscar(produtos, {"$or": [
                    {"tipo": opcao_tipoAmbos.lower()},
                    {"subtipo": opcao_tipoAmbos.lower()},
                    {"subtipo": opcao_tipoAmbos.lower().capitalize()}
                ]})

            ## Ordem numérica
            # Item 2 - todos, por preço
            elif opcao_1 in numTodos["normal"]:
                busca = Busca.buscar(produtos, {}, {"_id": 0}, "preco")
            elif opcao_1 in numTodos["inv"]:
                busca = Busca.buscar(produtos, {}, {"_id": 0}, "preco", -1)

            # Item 5 - definir preço máximo, por preço
            elif opcao_1 in L.unirListas([num["precoMax"]["normal"],\
                num["precoMax"]["inv"]]):
                userInput = "{}{}{}: ".format(
                    T.espacar(margem), m["precoMax"], m["voltar"]
                )
                maximo = Busca.digitarNumero(userInput, m["precoMaxErr"])
                if not maximo:
                    return Busca.menuBusca(self, o, m)
                if opcao_1 == "5":
                    busca = Busca.buscar(produtos,
                    {"preco": {"$lte": maximo}},\
                        {"_id": 0}, "preco")
                else:
                    busca = Busca.buscar(produtos, {"preco": {"$lte": maximo}},\
                        {"_id": 0}, "preco", -1)

            # Item 6 - definir preço mínimo, por preço
            elif opcao_1 in L.unirListas([precoMin["normal"], precoMin["inv"]]):
                userInput = "{}{}{}: ".format(
                    T.espacar(margem), m["precoMin"], m["voltar"]
                )
                minimo = Busca.digitarNumero(userInput, m["precoMinErr"])
                if not minimo:
                    return Busca.menuBusca(self, o, m)
                if opcao_1 in precoMin["normal"]:
                    busca = Busca.buscar(
                        produtos, {"preco": {"$gte": minimo}}, {"_id":0},
                        "preco"
                    )
                else:
                    busca = Busca.buscar(produtos, {"preco": {"$gte": minimo}},\
                                {"_id":0}, "preco", -1)

            # Item 56 - Definir preços máximo e mínimo, por preço
            elif opcao_1 in L.unirListas([precoAmbos["normal"], precoAmbos["inv"]]):
                userInput = "{}{}{}: ".format(
                    T.espacar(margem), m["precoMax"], m["voltar"]
                )
                maximo = Busca.digitarNumero(userInput, m["precoMaxErr"])
                if not maximo:
                    return Busca.menuBusca(self, o, m)
                userInput = "{}{}{}: ".format(
                    T.espacar(margem), m["precoMin"], m["voltar"]
                )
                minimo = Busca.digitarNumero(userInput, m["precoMinErr"])
                if not minimo:
                    return Busca.menuBusca(self, o, m)
                while maximo <= minimo:
                    print("{}{}".format(
                        T.espacar(margem), m["precoMaxMinErr"]
                    ))
                    minimo = Busca.digitarNumero(userInput, m["precoMinErr"])
                    if not minimo:
                        return Busca.menuBusca(self, o, m)
                if opcao_1 in precoAmbos["normal"]:
                    busca = Busca.buscar(produtos,
                        {"preco": {"$lte": maximo, "$gte": minimo}},\
                            {"_id":0}, "preco")
                else:
                    busca = Busca.buscar(produtos,
                        {"preco": {"$lte": maximo, "$gte": minimo}},\
                            {"_id":0}, "preco", -1)

            return (opcao_1, busca)

        else:
            ## Opção inválida
            print("{}\n".format(m["opcaoInvalida"]))

        return Busca.menuBusca(self, o, m)

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

    def buscarProdutos(self):
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

        termosBusca = Busca.menuBusca(self, opcoes, mensagens)
        if not termosBusca:
            return
        opcao, busca = termosBusca[0], termosBusca[1]

        print()

        alf = opcoes["ordem"]["alf"]

        alfabeticaNormal, alfabeticaInversa = [
            alf["todos"]["normal"], alf["tipo"]["normal"],
            alf["subtipo"]["normal"], alf["tipoAmbos"]["normal"]
        ], [
            alf["todos"]["inv"], alf["tipo"]["inv"],
            alf["subtipo"]["inv"], alf["tipoAmbos"]["inv"]
        ]

        resultado = Lista(busca)

        # 1 Ordem alfabética
        if opcao in L.unirListas(alfabeticaNormal):
            resultado.imprimirListaProdutos("–", 1, "nome")
        # 2 Ordem alfabética inversa
        elif opcao.lower() in L.unirListas(alfabeticaInversa):
            resultado.imprimirListaProdutos("–", 1, "nome", 1)
        # * Demais casos: mongoDb já traz ordenado
        else:
            resultado.imprimirListaProdutos("–")
        print()
        Busca.novaBusca(self)
    
class Lista:
    def __init__(self, lista):
        self.lista = lista

    def criarListaProdutos(self, ord=False, key="", inv=0):
        lista = list(self.lista)
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

    def listarProdutos(listaProdutos, maiorItem, larguraMinimaCol1):
        for i in listaProdutos:
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

    def imprimirListaProdutos(self, separador, ord=False, key="", inv=0):
        assert len(separador) == 1
        listaProdutos = Lista.criarListaProdutos(self, ord, key, inv)

        if not listaProdutos:
            return print("Nenhum resultado.")
        else:
            print("Itens encontrados: {}\n".format(len(listaProdutos)))

        maiorItem1 = L.analisarListaDict(listaProdutos, ["nome"])
        maiorItem2 = L.analisarListaDict(listaProdutos, ["preco"])

        titulos = ["Nome", "Preço"]
        larguraMinimaCol1 = len(titulos[0])

        tamanhoSeparacao1, tamanhoSeparacao2 = \
            maiorItem1 - len(titulos[0]) + 1, maiorItem2 - len(titulos[1]) - 3

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

        Lista.listarProdutos(listaProdutos, maiorItem1, larguraMinimaCol1)

def main():
    mongoURL = "mongodb://127.0.0.1:27017"

    dados = Dados(mongoURL)
    if dados.verificarBusca():
        client = pymongo.MongoClient(mongoURL)
        with client:
            db = client.test
        buscaFrutas = Busca(db)
        buscaFrutas.buscarProdutos()
    else:
        return

if __name__ == "__main__":
    main()
