def squares(n):
    if n < 1:
        return 1
    
    squares(n-1)
    print(n*n)

squares(4)