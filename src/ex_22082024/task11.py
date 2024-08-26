# Task11:
# ✅ Fibonacci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

# logic building
# 1. i/p = one number -->int o/p --> series
# 2 rough logic --> a= 0, b=1 , b= b+a

series_number = int(input("enter a number\n"))
for series_number in range(0, series_number + 1):
    a, b = 0, 1
a, b = b, a + b

print(a, b)
