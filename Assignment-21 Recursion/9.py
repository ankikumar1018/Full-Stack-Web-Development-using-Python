def multiple(n, i):

    '''
        n = number of multiples
        i = given number
    '''

    if n < 1:
        return 1
    
    multiple(n - 1, i)
    print(n * i)

multiple(n = 10, i= 5)