# ✅ Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
#
# Given three input values representing the lengths of the sides,
#
# determine if the triangle is equilateral (all sides are equal),
#
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
#
# Use an if-else statement to classify the triangle.

 #1logic building
# user input->data type ->3 float
# o/p data type->string user stating its type

# 2 rough logic
#enter the length of side1 ,side 2, side3
#if cond1  side1==side2==side3 print equi
#cond2 (side1==side2 and side1!=side3  or (side2==side3 or side 2!=side3) or (side1 =side3 or side1!=side2) print isoc
#print iso

#side1 != side2 or side1 !=side 3 or side2 !+side3 print scalene

side1=float(input("Enter the first side\n"))
side2=float(input("Enter the second side\n"))
side3=float(input("Enter the third side\n"))
if side1==side2==side3:
    print("It is a equilateral triangle")
elif side1==side2 and side1!=side3 or side2==side3 and side2!=side1 or side1==side3 and side1!=side2 :
    print("It is a isosceles triangle")
else:
    print("It is a scalene triangle")



