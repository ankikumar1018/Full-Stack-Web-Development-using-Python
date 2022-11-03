num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def lcm(num1, num2):

    if num1 > num2:
        greater_num = num1
        lesser_num = num2
    else:
        greater_num = num2
        lesser_num = num1

    mul = num1 * num2
    for i in range(greater_num, mul + 1):
        if i % lesser_num == 0 and i % greater_num == 0:
            return i

print(lcm(num1, num2))