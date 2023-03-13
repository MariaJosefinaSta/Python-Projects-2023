# The calculator should check if a number has already been entered.
# If they have already entered a number they will ask you to enter an operation.
# Then ask to enter a second value and the operator.
# And the result will be assigned as the first value you enter into the calculator for a next operation.

print("Welcome to the calculator")
print("To exit type exit")
print("You can add, subtract, divide or multiply")

result = ""

while True:
    if not result:
        result = input("Enter number")
        if result.lower() == "Exit":
            break
        result = int(result)
    op = input("Enter operation: ")
    if op.lower() == "Exit":
        break
    n2 = input("Enter next number")
    if n2.lower() == "Exit":
        break
    n2 = int(n2)

    if op.lower() == "Sum":
        result += n2
    elif op.lower() == "Subtraction":
        result -= n2
    elif op.lower() == "Divide":
        result /= n2
    elif op.lower() == "Mulitply":
        result *= n2
    else:
        print("Non-valid operation")
        break

    print(f"The result {result}")
