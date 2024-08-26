# conditions and loops
# syntax
# if condition:
#     (code you want to execute if condition is true)
#
# else:
#     (code you want to execute if condition is true)
# write a program to take a user age and let him knoe if he can go to club

# 1logic building
# user input->data type ->int
# o/p data type->string user can go or not

# 2 rough logic
# if age?25 print go
# hif age<25  cant go
# write logic


age = int(input("Enter the age\n"))
if age >=25:
    print(f"you can go at this age ->{age}")
else:
    print(f"you cant go at this age->{age}")
