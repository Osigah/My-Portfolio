from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    should_continue = True
    while should_continue:
        for i in operations:
            print(i)
        op = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        calc = operations.get(op)
        if calc:
            result = calc(num1, num2)
            print(f"{num1} {op} {num2} = {result}")
        else:
            print("Invalid Operation")
            continue
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = result
        else:
            should_continue=False
            print("\n" * 20)
            calculator()

calculator()


















