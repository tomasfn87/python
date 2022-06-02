import sys

def vertical(word):
    if len(word) == 1:
        print(word)
    else:
        print(word[0])
        return vertical(word[1:])

def reverse_vertical(word):
    if len(word) == 1:
        print(word)
    else:
        print(word[-1])
        return reverse_vertical(word[:-1])

if __name__ == '__main__':
    input = sys.argv[1]
    vertical(input)
    print()
    reverse_vertical(input)
