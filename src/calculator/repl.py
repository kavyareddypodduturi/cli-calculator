from calculator.operations import add, subtract, multiply, divide


def main():
    print("Simple Calculator")
    print("Type +  -  *  / to calculate")
    print("Type 'q' to quit")

    while True:
        op = input("\nEnter operation: ")

        if op.lower() == "q":
            print("Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result =", add(num1, num2))
        elif op == "-":
            print("Result =", subtract(num1, num2))
        elif op == "*":
            print("Result =", multiply(num1, num2))
        elif op == "/":
            print("Result =", divide(num1, num2))
        else:
            print("Invalid operation")


if __name__ == "__main__":
    main()
