user_input = input("Enter the user type: manager, guest or admin\n")

match user_input:
    case "manager":
        print("hello manager")
    case"guest":
        print("hello guest")
    case _:
        print("incorrect input")
