def palindrome(mystr):
    if mystr == mystr[::-1]:
        return "String is Palindrome"
    else:
        return "String is not Palindrome"

print(palindrome('eye'))