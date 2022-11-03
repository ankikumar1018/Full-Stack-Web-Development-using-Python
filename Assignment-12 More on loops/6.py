def prime(num):

    count_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            count_list.append(i)

    if len(count_list) == 2 and num > 0:
        return 'prime'
number = int(input("Enter the Nth number: "))
for i in range(1, number + 1):
    if prime(i) == 'prime':
        print(i, end=' ')