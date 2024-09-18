# sum of three numbers

num1 = int(input("enter the 1st number"))
num2 = int(input("enter the 2nd number"))
num3 = int(input("enter the 3rd number"))


# def addthree(a, b, c):
#     return(a+b+c)

# output= addthree(num1, num2, num3)
# print(f"result is {output}")

output = lambda a,b,c: a+b+c
print(output(num1,num2,num3))




