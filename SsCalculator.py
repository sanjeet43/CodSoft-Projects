print("\n*** Welcome to our Calculator App.***")
print("\n*** INSTRUCTION ***")
print('''
1) + for Addition.
2) - for Subtraction.
3) * for Multiplication.
4) / for Division.
''')

def calculate(operator, num1, num2):
    switch = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Cannot divide by zero."
    }
    return switch.get(operator, "Invalid operator.")

operators = ['+', '-', '*', '/']

while True:
    operator = input("\nEnter the operator ('+', '-', '*', '/'): ")
    if operator in operators:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))
        
        result = calculate(operator, num1, num2)
        print(f"The result of {num1} {operator} {num2} = {result}")
        
        choice = input("Want to continue or not? (y/n): ")
        if choice.lower().endswith('n'):
            print("Thank you for using our calculator. Goodbye!")
            break
    else:
        print("Invalid Input. Try Again.")