# MATCH STATEMENT
# switch in java
# match the op and execute
# python >3.10
# Match syntax
# case pattern1:
# #code block 1
# case pattern2:
# #code block 1

# browser_name = input("Enter the browser name \n")
# browser_name=browser_name.lower()
# case "firefox":
# print("execute the firefox code")
# case "safari":
# print("execute the firefox code")
# case _:
# print("browser not found!")

# # Write a automation program to ask a user which browser he needs for automation
browser_name = input("Enter the browser name \n")
browser_name = browser_name.lower()
match browser_name:
    case "Firefox":
        print("Execute the firefox code")
    case "safari":
        print("Execute the Chrome code")
    case _:
        print("browser not found")