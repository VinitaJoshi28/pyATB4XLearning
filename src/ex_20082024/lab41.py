# Grade calculator
# white a prgram that calculates and display a letter  grade on the basis of the numerical score
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# E: 0-59

# Logic building
# i/p --> score ->int
# o/p --> string

score = int(input("Enter the score\n"))

if score >= 90 and score <= 100:  # simplfied chaining if 90 <= score <= 100:
    grade = "A"
    print("Grade is ", grade)
elif score >= 80 and score <= 89:
    grade = "B"
    print(f"Grade is : {grade}")
elif score >= 70 and score <= 79:
    grade = "C"
    print(f"Grade is {grade}")
elif score >= 60 and score <= 69:
    grade = "D"
    print(f"Grade is {grade}")
elif score >= 50 and score <= 59:
    grade = "E"
    print(f"Grade is {grade}")
elif score >=100:
    print("You are superman")

else:
    grade = "F"
    print(f"grade is {grade}")
