# simple calculator 
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#addition
if choice == 1:
    print("Result =", num1 + num2)
#subtraction
elif choice == 2:
    print("Result =", num1 - num2)
#multiplication
elif choice == 3:
    print("Result =", num1 * num2)
#division
elif choice == 4:
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")
#invalid choice
else:
    print("Invalid choice! Please select between 1-4.")