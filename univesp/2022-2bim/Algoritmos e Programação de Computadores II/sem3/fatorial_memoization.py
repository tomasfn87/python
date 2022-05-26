m = dict()
def fat_mem(n):
    if n == 0:
        return 1
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = n * fat_mem(n-1)
        return m[n]

print(fat_mem(10))