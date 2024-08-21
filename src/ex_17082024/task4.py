### Task #4
#Write a Python program to calculate the area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)
import math

radius =float (input("Enter the radius\n"))
area=math.pi*math.pow(radius,2)
area2= 3.14 * (radius**2)
print(f"area of the circle:{area:.2f}")
print(f"area of the circle:{area2:.2f}")



