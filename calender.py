import calendar
year=int(input("Enter your year: "))
month=int(input("Enter your month: "))
cal = calendar.month(year,month)    #function month gives the calendar
print(cal)