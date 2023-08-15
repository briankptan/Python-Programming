#Input

again = "y"

while again == "y":

    calc = input("\nEnter single-digit calculation:")

    num1 = float(calc[0])
    #Ask for first num, float
    #num1 = float(input("\nEnter num1: "))

    operator = calc[1]
    #Ask for operator
    #operator = input("Enter operator: ")

    num2 = float(calc[2])
    #Ask for second num, float
    #num2 = float(input("Enter num2: "))

    #boolean datatype: True or False
    isValid = True

    #Processing
    if operator == "+":
        result = num1 + num2
        
    elif operator == "-" :
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
    if isValid == True:
        print("\nResult: ", format(result, "0.2f"))

    again = input("\nAgain? y/n: ")

done = input("\nGoodbye. Press Enter to exit")
