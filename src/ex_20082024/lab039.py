#problem to find max

#logic building

#Step1 : 1. user input -> int -> 2 integers
#2. output -> print int that is max
#3 input method
#4 31.33 and 44.33

num1= float(input("Enter the 1st number: \n"))
num2= float(input("Enter the 2nd number: \n"))
if num1 > num2:
    print(f"the bigger number is {num1}")
else:
    print(f"The bigger number is {num2}")

print (f"the maximum number is : {max(num1,num2)}")