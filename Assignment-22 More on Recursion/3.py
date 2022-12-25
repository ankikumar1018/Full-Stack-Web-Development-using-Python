def evenN(n):
    if n < 1:
        return 0
    s = (2*n) + evenN(n-1)
    return s

print(evenN(4))