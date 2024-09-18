# Task11:
# ✅ Fibonacci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

# logic building
# 1. i/p = one number -->int o/p --> series
# 2 rough logic --> a= 0, b=1 , b= b+a

fib = int(input("enter a number\n"))
a = 0
b = 1
if (fib == 0):
    print(0)
elif (fib == 1):
    print(0)
else:
    for i in range(2, fib + 1):

        print(f"fibonacci is {fib}")
