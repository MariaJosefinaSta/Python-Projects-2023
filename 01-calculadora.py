# lo primero es obtener una forma para obtener datos que ingrese el usuario

n1 = input("ingresa primero número")
n2 = input("ingresa segundo número")

print(n1, n2)

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
division = n1 / n2

# print(f {division} {es el resultado de la dividir}) MAL

mensaje = f"""
Para los números {n1} y {n2}.
el resultado de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado de la multi es {multi}.
el resultado de la división es {division}.
"""
print(mensaje)
