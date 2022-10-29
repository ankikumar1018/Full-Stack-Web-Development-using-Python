string1 = input("Enter first String: ")
string2 = input("Enter second String: ")

match string1, string2:
    case (string1,string2) if string1 == string2:
        print("Both string are Identical")
    case (string1,string2) if string1 < string2:
        print("First string comes first than second String")
    case (string1,string2) if string1 > string2:
        print("Second string comes first than first String")