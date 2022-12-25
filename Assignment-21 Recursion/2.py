def printN(n):
    if n>0:
        print(n, end=' ')
        printN(n-1)
        

printN(5)