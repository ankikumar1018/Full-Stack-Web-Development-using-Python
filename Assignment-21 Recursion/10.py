def reverse(number):
  if number < 10:
    return number
  else:
    return int(str(number % 10) + str(reverse(number // 10)))

print(reverse(123))