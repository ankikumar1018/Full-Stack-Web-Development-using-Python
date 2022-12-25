def sumN(n):
    if n == 1:
        return 1
    elif n < 1:
        return 'Number numst be greater than 0'
    
    s = n + sumN(n-1)
    return s

print(sumN(5))