start = int(input("Enter the bigining value: "))
end = int(input("Enter the ending value: "))

for n in range(start + 1, end + 1):
    isPrime = True
    for i in range(2, n - 1):
        if n % i == 0:
            isPrime = False
    if isPrime:
        print(n)