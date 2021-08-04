nome = "poesia.txt"    # poderia ser um input("Digite o nome do arquivo: ")

with open(nome, 'r', encoding='utf-8') as arq_entrada:
    # CORPO DO WITH
    conteudo = arq_entrada.read()

# continue o programa usando conteudo
print(conteudo)

name = "strings_and_files.txt"    # poderia ser um input("Digite o nome do arquivo: ")

with open(name, 'r', encoding='utf-8') as entry_file:
    content = entry_file.read()

print(content)