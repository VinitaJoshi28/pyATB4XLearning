# add sum of 3 number

num1 = int(input("enter first num\n"))
num2 = int(input("enter sec num\n"))
num3 = int(input("enter third num\n"))


# result=num1+num2+num3
# print(f"the result is {result}")

def result_three_numbers(n1, n2, n3):
    return n1 + n2 + n3


result= result_three_numbers(num1, num2, num3)
print(f"the result of 3 numbers is {result}")
