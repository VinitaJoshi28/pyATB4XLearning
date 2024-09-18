# #user defined
# 1. they cant return --> non -return
# 2. They can return something
# some paramters
# they dont parameters or arguments

# non return type example --> dont return any value--->no return type and no parameters/rguments (NRNP)
def greet():
    print("hi")


result = greet()
print(result)


# 2. no return type with arguments

def greet_by_name(name):
    print("hi", name)


greet_by_name("vini")


# no return with default arguments

def greet_people_default(name="vini"):
    print("hi", name)


greet_people_default()


def multiple_arguments(name1="A", name2="B", name3="C"):
    print(name1, name2, name3)


multiple_arguments()
multiple_arguments(name1="Amu", name2="scarlett", name3="ginni")


# 4. argument with return type

def sum_two_numbers_default(num1=100, num2=200):
    return num1 + num2


# result = sum_two_numbers_default()


# def sum_nums(num1, num2):
#     return num1 + num2


result = sum_two_numbers_default(2,3)
print(result)
result = sum_two_numbers_default()

print(result)
