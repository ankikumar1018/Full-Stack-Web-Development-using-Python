def evenN(n):
    
    if n < 1:
        return 1
    print(2*n)
    evenN(n - 1)
    

evenN(5)