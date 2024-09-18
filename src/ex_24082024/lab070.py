# num1= int(input("enter the first number"))
# num2= int(input("enter the sec number"))

def sum_threenum(a,b=1,c=3):    # set the value of c as default
    return a+b+c

result1=sum_threenum(10,20)
print(result1)
result1=sum_threenum(30,40)
print(result1)
result1=sum_threenum(30)
print(result1)
result1=sum_threenum(a=10, c=2)
print(result1)