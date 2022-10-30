n = int(input("Enter a number: "))
for i in range(1, n + 1):
    match i:
        case i if i % 2 == 0:
            print(i)