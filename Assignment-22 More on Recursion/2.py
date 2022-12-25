def oddN(n):
    if n < 1:
        return 0
    s = (2*n - 1) + oddN(n-1)
    return s

print(oddN(4))