given_number = int(input("Enter the number: "))
digit_list = []
while given_number != 0:
    k = given_number % 10
    digit_list.append(k)
    given_number = (given_number - k) // 10
digit_list.reverse()
print(digit_list)