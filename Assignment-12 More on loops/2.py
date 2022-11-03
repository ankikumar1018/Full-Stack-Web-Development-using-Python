num = int(input("Enter a number: "))

count_list = []

for i in range(1, num + 1):
    if num % i == 0:
        count_list.append(i)

if len(count_list) == 2 and num > 0:
    print("Prime Number")

else:
    print("Not a Prime Number")
