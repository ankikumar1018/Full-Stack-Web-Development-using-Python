def factorial(n):
    if n == 1:
        return 1
    s = n * factorial(n-1)
    return s

print(factorial(5))