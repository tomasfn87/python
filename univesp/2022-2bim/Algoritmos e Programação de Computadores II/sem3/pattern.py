import sys

def pattern(n, char):
    if n == 0:
        return
    elif n == 1:
        print(char[0])
    else:
        pattern(n-1, char)
        print(char[0] * n)
        return pattern(n-1, char)

if __name__ == '__main__':
    input = sys.argv
    pattern(int(input[1]), input[2])