lista = ['Alicia', 1998, 'Bob', 1990, 'Carlos', 1986, 'David', 2001]

""" for cliente in lista:
    nombre = cliente
    nacimiento = cliente + 1
    print(nombre, nacimiento) """  # No, ya que no declara un string de tipo int

for i in range(0, len(lista), 2):
    nombre = lista[i]
    nacimiento = str(lista[i+1])
    print(nombre, nacimiento)

lista = ['Alicia', 'Bob', 'Carlos', 'David']

while len(lista) > 0:
    ultimo_cliente = len(lista) - 1
    cliente = lista.pop(ultimo_cliente)
    print(cliente)

d = ['Alicia', 'Bob', 'Carlos', 'David']    # lista de dueños
m = ['Pelusa', 'Luke', 'Mickey', 'Madonna']  # lista de mascotas

for i in range(len(d)):
    print(d[i], m[i])

lista = ['soleado', 'nublado', 'soleado', 'lluvia',
         2.4, 'lluvia', 0.1, 'nublado', 'lluvia', 0.8]

""" suma = 0
for i in lista:
    if i != 'soleado' or i != 'nublado' or i != 'lluvia':
        suma += i
print(suma) """

suma = 0
for i in range(len(lista)):
    if lista[i] == 'lluvia':
        suma += i+1  # No se puede acer una suma sin un valor de tipo número
print(suma)

lista = [['A1', 'B1', 'C1', 'D1'],
         ['A2', 'B2', 'C2', 'D2'],
         ['A3', 'B7', 'C3', 'D3'],
         ['A4', 'B4', 'C4', 'D4']
         ]

lista[2][1] = 'B3'

votos = [['Alicia', 35],
         ['Bob', 42],
         ['Carlos', 29],
         ['David', 33],
         ]

""" mejor = max(votos)
print(mejor[0]) """

mejor = ['', 0]
for candidato in votos:
    if candidato[1] > mejor[1]:
        mejor = candidato
print(mejor[0])

lista = [[-1, 2, -5, 40],
         [9, 65, -6, -34],
         [0, -4, 9, 2]
         ]

for fila in lista:
    for dato in fila:
        if dato < 0:
            dato = 0

ingredientes_amigos = [
    ['Pan', 'Salchichas', 'Mostaza', 'Ketchup'],  # ingr. amigo 1
    ['Pan', 'Tomate', 'Chucrut'],  # ingr. amigo 2
    ['Ketchup', 'Salchichas'],  # ingr. amigo 3
    ['Chucrut', 'Pan']  # ingr. amigo 4
]

ingredientes_favoritos = ['Pan', 'Tomate', 'Salchichas',
                          'Chucrut', 'Mostaza', 'Ketchup', 'Mayonesa', 'Palta']

for amigo in ingredientes_amigos:
    for ingrediente in amigo:
        if ingrediente in ingredientes_favoritos:
            ingredientes_favoritos.remove(ingrediente)
# Imprime la lista con los ingredientes favoritos que no se repitan en la lista de los ingredientes de los amigos
print(ingredientes_favoritos)
