given_list = [1,1,2,2,2,3,4,5]
obj = []
for i in given_list:
    if i not in obj:
        obj.append(i)
for i in obj:
    print(f'Frequency of {i} is {given_list.count(i)}')