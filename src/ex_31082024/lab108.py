class DOG:
    # A
    name = None
    breed = None
    color = None
    # B
    def sleep(self):
        print("I love to sleep")

    def bark(self):
        print("I love to bark")
    def eat(self,food):
        print(food)

dog1 = DOG()
dog1.name = "Pluto"
dog1.breed = "Mastiff"
dog1.color = "Brown"
print(dog1.name)
dog1.sleep()

dog2 = DOG()
dog2.name = "Marz"
dog2.breed = "Bulldog"
dog2.color = "black"
print(dog2.name)
dog2.sleep()
dog2.eat("pedigree")