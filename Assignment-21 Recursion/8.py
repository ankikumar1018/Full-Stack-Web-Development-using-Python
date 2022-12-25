def cubes(n):
    if n < 1:
        return 1
    
    cubes(n-1)
    print(n**3)

cubes(4)