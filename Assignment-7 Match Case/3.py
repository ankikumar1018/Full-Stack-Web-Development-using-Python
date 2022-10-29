x = int(input("Enter the 1st side length of triangle = "))
y = int(input("Enter the 2nd side length of triangle = "))
z = int(input("Enter the 3rd side length of triangle = "))
print()

operation = ''
while operation != 'd':
    operation = input("Select among following operation:\na. Check Isosceles Traingle\nb. Check Right Angle Traingle\nc. Check Equilateral Traingle\nd. Exit\n\nYour Choice: ")
    match operation:

        case 'a':
            if x == y == z:
                print("Equilateral Traingle")
            else:
                print("Not Equilateral Traingle")

        case 'b':
            if (x**2==y**2+z**2) or (y**2==x**2+z**2) or (z**2==x**2+y**2):
                print("Right Angle Traingle")
            else:
                print("Not Right Angle Traingle")
        
        case 'c':
            if (x==y!=z) or (x==z!=y) or (y==z!=x):
                print("Isosceles Traingle")
            else:
                print("Not Isosceles Traingle")
        case 'd':
            print("Program Quit🙋‍♂️🙋‍♂️")