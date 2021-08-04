#'''
fh = open("sample-file_01.txt", "r")

'''print(fh.readline(7))
print(fh.readline())
print(fh.readline())'''
#print(fh.readlines()[9])
for line in fh:
    print(line, end="")
    print("It has", len(line.split(' ')),"words.\n")

fh.close()
'''

with open("sample-file_01.txt", "r") as fh:
    print(fh.read())
'''