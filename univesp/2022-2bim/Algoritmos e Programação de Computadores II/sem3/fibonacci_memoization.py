m = dict()
def fib_mem(n):
    if n < 2:
        return n
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = fib_mem(n-1) + fib_mem(n-2)
        return m[n]

print(fib_mem(10))