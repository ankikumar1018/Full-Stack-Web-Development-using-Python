def squareN(n):
    if n == 1:
        return 1
    elif n < 1:
        return 'Number numst be greater than 0'
    
    s = n**2 + squareN(n-1)
    return s

print(squareN(3))