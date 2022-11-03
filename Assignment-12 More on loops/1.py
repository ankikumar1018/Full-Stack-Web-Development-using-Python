number = int(input("Enter a number: "))
conv_num = str(number)[::-1]
new_num = int(conv_num)
print(type(new_num), new_num)