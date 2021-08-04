nome = "poesia.txt"    # poderia ser um input("Digite o nome do arquivo: ")

with open(nome, 'w', encoding='utf-8') as arq:
    # CORPO DO WITH
    arq.write("    O poeta é um fingidor.      \n")
    arq.write("    Finge tão completamente     \n")
    arq.write("    Que chega a fingir que é dor\n")
    arq.write("    A dor que deveras sente.    \n")
    arq.write("                Fernando Pessoa.\n")

name = "strings_and_files.txt"

with open(name, "w", encoding="utf-8") as arq:
    arq.write("   Several lines\n")
    arq.write("   of strings\n")
    arq.write("   written to our file:\n")
    arq.write("   strings_and_files.txt\n")