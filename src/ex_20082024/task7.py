# Create a program that determines whether a given year is a leap year.
#
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# better way of saying-----
# If a year is divisible by 4 and not by 100, it is a leap year,
# unless it is divisible by 400 (which makes it a leap year regardless).
# # Use an if-else statement to make this determination.

# rough logic

# leapyear/4 and remainder is zero-> cond1
# cond2 leap/400 and reminder =zero  and year % 400 == 0

year = int(input("Enter the year\n"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} not a leap year")