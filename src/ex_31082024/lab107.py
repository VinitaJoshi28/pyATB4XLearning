class Person:
    #attributes
    id = None
    name = None
    age = None
    email = None

#behavior
def talk(self):   #no arg no return
    print("I can talk")


def sleep(self,name):
    print("Iam sleeping")  #arg with no return type
    print("sleep", name)

def sleep2(self,name):
    print("iam method")  #arg with return type
    return None

#create an object with the class
#object reference = classname()

vini = Person()
vini.id = "22"
vini.name = "vinita"
vini.age = 33
print(vini.id)
print(vini.name)
print(vini.age)


manoj=Person()
manoj.name = "manoj"
manoj.email = "manoj@gmail.com"

