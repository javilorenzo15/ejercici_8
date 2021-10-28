lista = []

while True:
    nombre = input("nombre:")
    if nombre == "fin":
        break
    numero_telefono = input("numero de telefono:")
    linea = {}
    linea["nombre"] = nombre
    linea["numero de telefono"] = numero_telefono
    lista.append(linea)
    for linea in lista:
        print("lista:\n",linea)