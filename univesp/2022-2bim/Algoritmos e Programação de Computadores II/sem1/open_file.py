infile = open('file.txt', 'r')
data = infile.readlines()
infile.close()

for line in data:
    operation_and_values = line.split(' ')
    operation = operation_and_values[0]
    values = operation_and_values[1:]

    if operation == 'Soma':
        total = eval(values[0])
        for i in range(1, len(values)):
            total += eval(values[i])    
        print(total)

    elif operation == 'Subtração':
        total = eval(values[0])
        for i in range(2, len(values)):
            total -= eval(values[i])
        print(total)