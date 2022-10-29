age = int(input("Enter your age: "))
if age < 10:
    print("Kid")
elif age < 20:
    print("Teen")
elif age < 40:
    print("Young")
elif age < 60:
    print("Experienced")
else:
    print("Senior Citizen")