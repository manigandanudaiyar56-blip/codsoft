
# CALCULATOR


while True:
    print("\n Basic Text Calculator")
    user_input = input("Enter calculation or 'exit': ")

    if user_input == "calculation":
        pass
    else:
        break

    operation = (input("Enter operator:"))

    n1 = int(input("Enter number1:"))

    n2 = int(input("Enter number2:"))

    if (operation == "+"):
        print(n1 + n2)
    elif (operation == "-"):
        print(n1-n2)
    elif (operation == "*"):
        print(n1*n2)
    elif (operation == "/"):
        print(n1/n2)
