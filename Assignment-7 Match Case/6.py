a_string = input("Enter the string: ")
space = ' '

match a_string:
    case a_string if space in a_string:
        print("Given string is a multi word string")
    case _:
        print("Given string is a single word string")
