def print_octal(n):
  if n == 0:
    return
  print_octal(n // 8)
  print(n % 8, end='')

print_octal(10)