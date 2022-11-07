def prime(number):
    i = 2
    flag = True
    if number > 1:    
        for i in range(2, number//2):
            if number % i == 0:
                flag = False
                return "Not Prime"
        else:
            return "Prime Number"
    else:
        return "Number should be greater than 1"

print(prime(1))