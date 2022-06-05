import sys

from pilha import Pilha

class Dec(Pilha):
    def __init__(self, numero):
        super().__init__()
        self.numero = int(numero)

    def decimal(self):
        return self.numero

    def binary(self):
        conta = self.numero
        while conta > 0:
            self.push(conta % 2)
            if conta <= 2:
                self.push(conta // 2)
                break
            conta = conta // 2
        binary = self.empty_me()
        result = ''
        for i in binary:
            result += str(i)
        return str(int(result))

    def octal(self):
        conta = self.numero
        while conta > 0:
            self.push(conta % 8)
            if conta <= 8:
                self.push(conta // 8)
                break
            conta = conta // 8
        octal = self.empty_me()
        result = ''
        for i in octal:
            result += str(i)
        return str(int(result))

    def hexadecimal(self):
        conta = self.numero
        while conta > 0:
            self.push(conta % 16)
            if conta <= 16:
                self.push(conta // 16)
                break
            conta = conta // 16
        hexadecimal = self.empty_me()
        result = ''
        for i in range(0, len(hexadecimal)):
            if hexadecimal[i] >= 10 and hexadecimal[i] <= 15:
                result += chr(hexadecimal[i]+55)
            if hexadecimal[i] >= 1 and hexadecimal[i] <= 9:
                result +=  str(hexadecimal[i])
            if hexadecimal[i] == 0 and i != 0: 
                result += str(hexadecimal[i])
        return result

if __name__ == '__main__':
    if len(sys.argv) > 2:
        inputs = sys.argv
    decimal = inputs[1]
    conversao = inputs[2]
    decimal = int(decimal)
    if conversao.strip() in ['2', '8', '16']:
        n=Dec(decimal)
        if conversao == '2':
            print(n.binary())
        elif conversao == '8':
            print(n.octal())
        else:
            print(n.hexadecimal())
    else:
        print('Digite o número decimal e a conversão desejada: 2, 8, ou 16')