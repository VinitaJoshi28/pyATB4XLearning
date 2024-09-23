# Class and Object Assignment

# Create a Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, printdetails,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.

class Employee:
    name = None
    age = None
    phone = None
    address = None
    eid = None

    def __init__(self):
        self.name = input("Enter the employee  name")
        self.phone = input("Enter the employee phone")
        self.eid = input("Enter the email")
        self.address = input("Enter the address")

    def walk(self):
        print("Iam walking")

    def talk(self):
        print("Iam talking")

    def print_details(self):
        print("Name is", self.name)
        print("phone is", self.phone)
        print("address is", self.address)
        print("eid is", self.eid)


emp1 = Employee()
emp2 = Employee()
emp1.print_details()
emp2.print_details()
