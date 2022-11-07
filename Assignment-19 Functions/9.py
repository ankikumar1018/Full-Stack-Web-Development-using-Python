def checkRange(number):
    if 1 <= number <= 100:
        return "Number is between 1 to 100"

    elif 101 <= number <= 1000:
        return "Number is between 101 to 1000"
    
    else:
        return "Number is greater than 1000"

print(checkRange(500))


