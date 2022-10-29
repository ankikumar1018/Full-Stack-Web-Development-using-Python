number = int(input("Enter a number: "))
match number:
    case 0:
        print("Entered number is Zero")
    case number if number < 0:
        print("Entered number is Negative")
    case number if number > 0:
        print("Entered number is Positive")