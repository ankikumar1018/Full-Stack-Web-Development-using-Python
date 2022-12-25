def digitSum(n):
    if n == 0:
        return 0
    sum = (n % 10) + (digitSum(n//10))
    return sum

print(digitSum(1234))