def is_leap(year):
    leap = False
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        # if the year is divisible by 400 or divisible by 4 but not by 100, it's a leap year
        leap = True
    
    return leap

year = int(input("Enter a year: "))
print(is_leap(year))