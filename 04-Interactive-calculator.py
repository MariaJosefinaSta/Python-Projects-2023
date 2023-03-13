# The calculator should check if a number has already been entered.
# If they have already entered a number they will ask you to enter an operation.
# Then ask to enter a second value and the operator.
# And the result will be assigned as the first value you enter into the calculator for a next operation.

print("Welcome to the calculator")
print("To exit type exit")
print("You can add, subtract, divide or multiply")

resultado = ""

while True:
    if not resultado:
        resultado = input("ingrese número")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingresa operación: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa el siguiente número")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "dividir":
        resultado /= n2
    elif op.lower() == "multiplicar":
        resultado *= n2
    else:
        print("Operación no válida")
        break
    print(f"El resultado es {resultado}")
