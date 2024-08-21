import math

print(math.pi)
print(math.pow(2,2))
print(math.sin(90))


age = 10

print( f"here is your string {age}")

#Write a Python program to calculate the area of the circle given its radius using the formula
#''' area = pi _r^2 (pi=3.14)

#Logic building formula
#Step1: Figure out the input and outputs

#input = r ->data type -> float or int
#pi=3.14
#power __ can you power function ** or any


#output = float =area , print area

#Step2 :
#rough logic = area = 3.14* pow(r,2)

#Step3 : write the logic

radius= float(input("Enter the radius\n"))
area = math.pi * math.pow(radius,2 )
area2= 3.14 * (radius**2)
area3=math.pi*pow(radius,2)
print(f"area is, {area:.2f}")
print("area is", area2)
print("area is", area3)



#  *  -> multiplication
#  ** -> power



