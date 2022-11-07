def cal_upper_lower(mystr):
    upper = 0
    lower = 0
    space = 0
    for i in mystr:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():
            space += 1
    return f'upper={upper}, lower={lower} and space={space}'

print(cal_upper_lower("Ankit Kumar Singh"))
        