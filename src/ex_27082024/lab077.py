def outer_function():
    val = 3

    def inner_function1():
        print(val)

    def inner_function2():
        print(val)
    inner_function1()
    inner_function2()

outer_function()
