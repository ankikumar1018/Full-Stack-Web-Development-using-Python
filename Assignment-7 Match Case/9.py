import calendar

class Year:
    def __init__(self, year):
        self.year = year

    def leap_year(self):
        if calendar.isleap(self.year) == True:
            return "Leap Year"
        else:
            return "Not a Leap Year"
    
    def century(self):
        if self.year % 100 == 0:
            return "Century Year"
        else:
            return "Not a Century Year"

input_year = int(input("Enter a year: "))
print(Year(input_year).leap_year())
print(Year(input_year).century())