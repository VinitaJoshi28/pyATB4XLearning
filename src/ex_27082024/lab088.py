def oddeven():
    num = int(input("enter the number"))

    if (num % 2 == 0):
        print("even")
    else:
        print("odd")


# oddeven()
#
# output = lambda num: "even" if num % 2 == 0 else "odd"
# print(output(6))

# output = lambda a, b, c: a + b + c
# print(output(2, 6, 7))

num = int(input("enter the number"))
output = lambda num: pow(num, 3)
print(output(num))
