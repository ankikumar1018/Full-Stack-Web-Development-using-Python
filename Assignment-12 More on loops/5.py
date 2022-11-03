def prime(num):

    count_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            count_list.append(i)

    if len(count_list) == 2 and num > 0:
        return "Prime"
    else:
        return "Not Prime"

number = int(input("Enter a number: "))
number += 1

while True:
    prime(number)
    if prime(number) == 'Prime':
        print("Prime Number: ", number)
        break
    else:
        number += 1
