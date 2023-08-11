#Input

again = "y"

while again == "y" or again == "Y":

    #Ask for first num, float
    num1 = float(input("\nEnter num1: "))

    #Ask for operator
    operator = input("Enter operator: ")

    #Ask for second num, float
    num2 = float(input("Enter num2: "))

    #boolean datatype. 
    isValid = True

    #Processing
    if (operator == "+"):
        result = num1 + num2

    elif (operator == "-"):
        result = num1 - num2

    elif (operator == "*"):
        result = num1 * num2

    elif (operator == "/"):
        if num2 == 0:
            print("Error: Divide by Zero")
            isValid = False
        else:
            result = num1 / num2

    else:
        print("Invalid operator")
        isValid = False

    #Output
    #if isValid == True:
    if isValid:
        print("\nResult: ", format(result, ".2f"))

    again = input("\nAgain? y/n: ")

hold = input("\nGoodbye. Press Enter to exit")
