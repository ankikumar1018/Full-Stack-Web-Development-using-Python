def oddN(n):
    
    if n < 1:
        return 1
    print(2*n - 1)
    oddN(n - 1)
    

oddN(5)