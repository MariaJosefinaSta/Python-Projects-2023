# The calculator should check if a number has already been entered.
# If they have already entered a number they will ask you to enter an operation.
# Then ask to enter a second value and the operator.
# And the result will be assigned as the first value you enter into the calculator for a next operation.

print("Welcome to the calculator")
print("To exit type exit")
print("You can add, subtract, divide or multiply")

resultado = " "

while True:
    if not resultado:
        resultado = input("ingrese número")
        if resultado.lower() == "salir":
            break
