import pymongo
import sys
sys.path.append('/home/morbi/filtering')
from texto import Texto as T

def listar_produtos(lista):
    for i in range(0, len(lista)):
        print(
            "{} {}\t| R${}".format(
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
    listar_produtos(list(arr))
    if end == True:
        print()

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

with client:
    db = client.test
    porNome = db.produtos.find().sort("tipo", 1)
    porPreco = db.produtos.find().sort("preco", -1)
    porPrecoMaiorOuIgualA5 = db.produtos.find({"preco": {"$gte": 5}}).sort("preco", 1)
    porPrecoMenorOuIgualA6 = db.produtos.find({"preco": {"$lte": 6}}).sort("preco", -1)
    porPrecoMaiorQue4MenorQue7 = db.produtos.find({"preco": {"$gt": 4, "$lt": 7}}).sort("preco", 1)

imprimirListaProdutos("Por nome (crescente)", porNome, "-")
imprimirListaProdutos("Por preco (descrescente)", porPreco, "-")
imprimirListaProdutos("Por preco: maior ou igual a 5 (crescente)", porPrecoMaiorOuIgualA5, "-")
imprimirListaProdutos("Por preco: menor ou igual a 6 (decrescente)", porPrecoMenorOuIgualA6, "-")
imprimirListaProdutos("Por preço: maior que 4 e menor a 7 (crescente)", porPrecoMaiorQue4MenorQue7, "-", False)
