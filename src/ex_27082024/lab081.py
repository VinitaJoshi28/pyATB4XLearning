def my_decorator(func):
    def wrapper():
        print("Open browser")

    func()
    print("close browser")

    return wrapper()


@my_decorator



def test_ui():
    print("iam running test")