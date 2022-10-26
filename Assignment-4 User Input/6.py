num1 = int(input())
num2 = int(input())
num3 = int(input())
s = (num1 + num2 + num3)/2
area = (s*(s-num1)*(s-num2)*(s-num3))**0.5
print(area)