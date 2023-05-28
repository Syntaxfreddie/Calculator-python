import math
print("Select an opretion to perform: ")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

operation = input()

if operation == "1":
        #code for add
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2":
        #code for subtraction
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("Result " + str(int(num1) - int(num2)))
elif operation == "3":    
        #code for multiplication
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("Result " + str(int(num1) * int(num2)))
elif operation == "4":
        #code for division
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        print("Result " + str(int(num1) / int(num2)))
else:
        print("Invalid Entry")    
