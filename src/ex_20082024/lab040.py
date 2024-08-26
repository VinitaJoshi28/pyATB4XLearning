# program to find max between 3 numbers

# Logic building

# user I/P ->  num1, num2, num3
# o/p---> print max int

# logic 1 condition -->if else
# more than 1 condition -> if elif else

# syntax
# #if condition 1:
#  print("do 1")
# elif condition2:
# print("do 2")
# elif condition3:
# print("do 3")
# elif condition4:
# print("do 4")
# else:
# print("print4")

num1 = int(input("Enter 1st number: \n"))
num2 = int(input("Enter 2nd number: \n"))
num3 = int(input("Enter 3rd number: \n"))
if num1 > num2 and num2 and num1 > num3:
    print(f"the greatest number is : {num1}")
elif num2 > num1 and num2 > num3:
    print(f"The greatest number is : {num2}")
else:
    print(f"The greatest number is : {num3}")

result = max(num1, num2, num3)
print(f"the result is: {result}")