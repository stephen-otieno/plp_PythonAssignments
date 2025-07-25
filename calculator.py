operators = print(
    "1.Addition(+) \n 2.Subtraction(-) \n 3.Multiplication(*) \n 4.Division(/) \n 5.Modulus(%)")

operator = int(input("Select an operator (1 - 5): "))


num1 = float(input("Enter 1st value: "))
num2 = float(input("Enter 2nd value: "))

if operator == 1:
    result = num1 + num2
    
    print("**********")
    print(f"{num1} + {num2} = {result}")
    print("**********")


elif operator == 2:
    result = num1 - num2
    
    print("**********")
    print(f"{num1} - {num2} = {result}")
    print("**********")




elif operator == 3:
    result = num1 * num2
    
    print("**********")
    print(f"{num1} * {num2} = {result}")
    print("**********")



elif operator == 4:
    if num2 == 0:
        print("Error! Can not divide by zero")
        exit()
    else:
        result = num1 / num2
        
        print("**********")
        print(f"{num1} / {num2} = {result}")
        print("**********")



elif operator == 5:
    if num2 == 0:
        print("Error! Can not find modulus by zero")
        exit()
    else:
        result = num1 % num2
        
        print("**********")
        print(f"{num1} % {num2} = {result}")
        print("**********")




# print("**********")

# print(f"Answer = {result}")


# print("**********")
