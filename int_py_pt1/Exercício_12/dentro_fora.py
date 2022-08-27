def check_cartesian(x, y):
    if -3 <= x <= 3 and 1 <=  y <= 2:
        print('dentro')
    elif -4 <= x <= -1 and 4 <= y <= 7:
        if -3 <= x <= -2 and 5 <=  y <= 6:
            print('fora')
        else:
            print('dentro')
    elif -4 <= (x  * -1) <= -1 and 4 <=  y <= 7:
        if -3 <= (x  * -1) <= -2 and 5 <=  y <= 6:
            print('fora')
        else:
            print('dentro')
    else:
        print('fora')

X = float(input('digite x: '))
Y = float(input('digite y: '))

check_cartesian(X, Y)