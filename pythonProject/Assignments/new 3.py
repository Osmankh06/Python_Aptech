def calculator():
    num1 = int(input("Enter number:"))
    for i in range(999):
        operator = input("Enter any operator:")
        if operator == " ":
            break
        num2 = int(input("Enter number:"))
        if operator == "*":
            num1 *= num2
        elif operator == "/":
            num1 /= num2
        elif operator == "+":
            num1 += num2
        elif operator == "-":
            num1 -= num2
        elif operator == " ":
            break
        else:
            print("Error")
        print("=", num1)

calculator()
