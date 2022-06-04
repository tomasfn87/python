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

print(f'({Dec(2047).hexadecimal()})16\t\t\t({Dec(2047).decimal()})10')
print(f'({Dec(2047).octal()})8\t\t\t({Dec(2047).decimal()})10')
print(f'({Dec(2047).binary()})2\t\t({Dec(2047).decimal()})10')
print(f'({Dec(4095).binary()})2\t\t({Dec(4095).decimal()})10')
print(f'({Dec(4095).octal()})8\t\t\t({Dec(4095).decimal()})10')
print(f'({Dec(4095).hexadecimal()})16\t\t\t({Dec(4095).decimal()})10')