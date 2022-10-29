'''

import calendar


month = input("Enter the month name: ")
year = int(input("Enter the year: "))
def is_leap_year(year):
    return calendar.isleap(year)

if month == 'September' or month == 'April' or month == 'June' or month == 'November':
    print(30)
elif month == 'January' or month == 'March' or month == 'May' or month== 'July' or month == 'August' or month == 'October' or month== 'December':
    print(31)
elif month == 'February' and is_leap_year(year) == True:
    print(29)
elif month == 'February' and is_leap_year(year) == False:
    print(28)
else:
    print('Blank')

'''

month = input("Enter the month name: ")

   
match month:

    case 'January':
        print(31)
    case 'March':
        print(31)
    case 'May':
        print(31)
    case 'July':
        print(31)
    case 'August':
        print(31)
    case 'October':
        print(31)
    case 'December':
        print(31)
    case 'September':
        print(30)
    case 'April':
        print(30)
    case 'June':
        print(30)
    case 'November':
        print(30)
    case 'February':
        print(28)