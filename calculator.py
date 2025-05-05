def Calc():
    first_number = input("Enter first number: ")
    second_number = input("Enter second Number: ")
    operation = input("Enter the operation: ")

    if (operation) == '+':
        return int(first_number) + int(second_number)
    elif operation == '-':
        return int(first_number) - int(second_number)
    elif operation == '*':
        return int(first_number) * int(second_number)
    elif operation == '/':
        if second_number == '0':
            return(f"Division by zero is not allowed")
        return int(first_number) / int(second_number)
    else:
        return(f"Operation not valid")
    
print(Calc())
