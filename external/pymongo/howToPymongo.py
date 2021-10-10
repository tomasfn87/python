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

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

with client:
    db = client.test
    produtosPorNome = db.produtos.find().sort("tipo", 1)
    produtosPorPreco = db.produtos.find().sort("preco", -1)
    
    print("Por nome (crescente)")
    print("--------------------")
    listar_produtos(list(produtosPorNome))
    print()
    print("Por preco (descrescente)")
    print("------------------------")
    listar_produtos(list(produtosPorPreco))