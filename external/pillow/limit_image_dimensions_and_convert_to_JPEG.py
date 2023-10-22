from PIL import Image
from sys import argv
import re

def main():
    if len(argv) < 3:
        print("Informe o caminho para uma imagem de entrada e o nome do arquivo de saída a ser salvo na pasta 'output'.")
        return
    imagem = argv[1]
    nome_arquivo_saida = argv[2]
    if re.match(r'[\/]', nome_arquivo_saida):
        print(r"O nome do arquivo de saída não pode possuir os caracteres '\' ou '/'.")
        return
    # remover a extensão do arquivo caso seja informada
    nome_arquivo_saida_sem_extensao = re.sub(r'\.\S*$', '', nome_arquivo_saida)
    output = f"./output/{nome_arquivo_saida_sem_extensao}.jpg"
    nova_imagem = redimensionar_imagem(imagem=imagem, largura_maxima=1366, altura_maxima=768)
    nova_imagem.save(output)
    print(f"Resultado salvo em {output}.")

def redimensionar_imagem(imagem, largura_maxima, altura_maxima):
    img = Image.open(imagem)
    img = img.convert('RGB')
    largura_original, altura_original = img.size
    nova_largura, nova_altura = largura_original, altura_original
    while nova_altura > altura_maxima or nova_largura > largura_maxima:
        if nova_altura > altura_maxima:
            nova_altura = altura_maxima
            nova_largura = int((largura_original / altura_original) * nova_altura)
        if nova_largura > largura_maxima:
            nova_largura = largura_maxima
            nova_altura = int((altura_original / largura_original) * nova_largura)
    img = img.resize((nova_largura, nova_altura))
    return img

if __name__ == '__main__':
    main()
