# Constructor
# automatically called when object is called
# sole purpose  to assign the value of n object
# Special function in class __init__()
class Dog:
    name = None

    def __init__(self, name):
        self.name = name

    def sleep(self, name):
        print("Sleeping", name)


dog1 = Dog("chow")
print(dog1.name)
dog1.sleep("chow")

dog2 = Dog("cow")
dog2.sleep("bulldog")
