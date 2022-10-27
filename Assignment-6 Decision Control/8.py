import math

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = math.sqrt(b ** 2 - 4 * a * c)


x = (-b + math.sqrt(d)) / (2 * a)
y = (-b - math.sqrt(d)) / (2 * a)
print("x = ",x, "y = ",y)

print("Roots are equal or not: ", abs(x) == abs(y))



