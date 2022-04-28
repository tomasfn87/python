m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        m[i][j] = int(input(f'Entre com o Valor da Matriz[{i}, {j}]:' ))
        if m[i][j] > 0:
            print('O elemento  é maior que zero: ', m[i][j])
        elif m[i][j] < 0:
            print('O elemento  é menor que zero: ', m[i][j])
        else:
            print('O elemento é zero')

for x in range(0, 3):
    for y in range(0, 3):
        print(m[x][y])