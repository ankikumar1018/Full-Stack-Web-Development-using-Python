first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
operation = int(input("Select among following operation:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n\nYour Choice: "))
match operation:
    case 1:
        print("Addition of two numbers is = ", first_num + second_num)
    case 2:
        print("Subtraction of two numbers is = ", abs(first_num - second_num))
    case 3:
        print("Multiplication of two numbers is = ", first_num * second_num)
    case 4:
        print("Division of two numbers is = ", first_num / second_num)
