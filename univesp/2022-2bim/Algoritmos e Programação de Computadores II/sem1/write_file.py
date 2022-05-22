outfile = open('write.txt', 'w')
n = 5
title = (f'Tabuada do {n}:')

separador = ''
for i in range(0, len(title)):
    separador += '-'

outfile.write(f'{title}\n')
outfile.write(f'{separador}\n')

count = 0
for i in range(0, n*10+1, 1):
    if i % n == 0:
        outfile.write(f'{count} X {n} = {i}\n')
        count += 1
    
outfile.close()