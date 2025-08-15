print(" Simple Calculator - Python Project")
print("""This is a basic calculator program that
performs addition, subtraction, multiplication,
and division based on user input.""")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = input("Enter an operation (+, -, *, /): ")

# Performing calculation based on the operation
if c == "+":
    print("Result:", a + b)
elif c == "-":
    print("Result:", a - b)
elif c == "*":
    print("Result:", a * b)
elif c == "/":
    # Prevent division by zero
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Incorrect operation entered.")
