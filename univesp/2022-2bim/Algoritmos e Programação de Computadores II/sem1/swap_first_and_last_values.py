def swap_first_and_last_values(list):
    if len(list) > 1:
        list[0], list[-1] = list[-1], list[0]
    

list_1 = ['Christopher', 'Charles', 'Bertrand']

print(list_1)
swap_first_and_last_values(list_1)
print(list_1)

list_2 = [11, 43, 55, 32, 790]

print(list_2)
swap_first_and_last_values(list_2)
print(list_2)