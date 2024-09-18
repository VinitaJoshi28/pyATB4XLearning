# decorators ---to modify the function without changing the source code
# it is used to wrap another function and extends its functionality

# two parts : wrap and call

def my_dec(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper()



@my_dec
def driving():
    print("driving")














def my_decorator(func):
    def wrapper():
        print("wear helmet, knee guard")
        func()
        print("safe driving")

    return wrapper()


# @my_decorator
# def driving_bike():
#     print("iam driving") @ my_decorator


@my_decorator







def driving_bike2():
    print("2iam driving")
