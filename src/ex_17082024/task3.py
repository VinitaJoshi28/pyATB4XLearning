# ### Task #3
# - Explain the difference between the = operator and the == operator in Python.
# = is the assignment operator and is used to asign the value to  variable or update a value
# for ex: int x=10, name="Vinita", list [a,b,c] = [1,2,3]
# == is a euality operator to compare two values
# for ex
a=12
b=13
print(a==b)
# - What does the ** operator do in Python, and how is it used?
# It is a power function
# - What does the ^ operator do in Python, and in what context is it commonly used?


 #What does the ** operator do in Python, and how is it used?
#n Python, the ** operator is used for exponentiation.
base=5
exponent=3
print(base**exponent)
#What does the ^ operator do in Python, and in what context is it commonly used?

# Python, the ^ operator is the bitwise XOR(exclusive OR) operator.It performs an
# XOR operation between corresponding
# bitsoftwonumbers.TheresultoftheXORoperation is 1 if thecorrespondingbitsoftheoperandsaredifferent, and 0 if
# they are the same
a=20  #in binary : 10100
b=10   #in binary : 1010
print(a^b) #output      11110
a = 10  # in binary: 1010
b = 4   # in binary: 0100
result = a ^ b
print(result)  # Output: 14 (in binary: 1110)