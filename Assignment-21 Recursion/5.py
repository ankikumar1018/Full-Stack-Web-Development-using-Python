def evenN(n):
    
    if n < 1:
        return 1
    evenN(n - 1)
    print(2*n)

evenN(5)