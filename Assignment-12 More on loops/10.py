def hcf(num1, num2):
    l = [num1, num2]
    greater_num = max(l)
    lesser_num = min(l)
    
    while True:
        q = greater_num % lesser_num 
        if q == 0:
            return lesser_num
        else:
            greater_num = lesser_num
            lesser_num = q
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(hcf(number1, number2))
