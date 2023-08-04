def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations available:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Enter 'exit' to end the calculator.")
    while True:
        operator = input("Enter the operation number (1/2/3/4) or 'exit': ")
        if operator == 'exit':
            print("Calculator terminated.")
            break
        if operator not in ('1', '2', '3', '4'):
            print("Invalid input. Please enter a valid operation number.")
            continue
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if operator == '1':
            print("Result: ", add(num1, num2))
        elif operator == '2':
            print("Result: ", subtract(num1, num2))
        elif operator == '3':
            print("Result: ", multiply(num1, num2))
        elif operator == '4':
            print("Result: ", divide(num1, num2))
if __name__ == "__main__":
    calculator()
