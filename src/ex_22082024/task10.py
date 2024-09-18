# Task #10 -
# ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

# input -> number ->int and o/p --> number 5
# rough logic -> result int--> fact=1
# num= num*(num-1)(num-2) .....(num

num = int(input("Enter a number for which you want the factorial: \n"))
fact = 1

for i in range(1, num + 1):
    print(i)  # This will print each number in the loop
    fact = fact * i  # Multiply the current value of fact by i

print(f"The factorial of {num} is {fact}")