#given year is leap year or not
def year(x):
    if (x% 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        print('Given year is a leap year')
    else:
        print('Given year is not a leap year')
print(year(2026))
print(year(2016))
