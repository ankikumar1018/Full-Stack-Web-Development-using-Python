def print_binary(n):
  if n == 0:
    return
  print_binary(n // 2)
  print(n % 2, end='')

print_binary(3)