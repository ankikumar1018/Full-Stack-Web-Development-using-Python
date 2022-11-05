# a = ("Java", "Python", "SQL", "C")
# a = a[::-1]
# print(a)

a = ("Java", "Python", "SQL", "C")

temp = list(a)
temp.reverse()
temp = tuple(temp)

print(temp)