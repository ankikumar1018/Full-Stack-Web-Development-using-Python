def cubeN(n):
    if n == 1:
        return 1
    elif n < 1:
        return 'Number numst be greater than 0'
    
    s = n**3 + cubeN(n-1)
    return s

print(cubeN(3))