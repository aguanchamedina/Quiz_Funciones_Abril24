# Construir una función que reciba un valor entero como parámetro y muestra la tabla de multiplicar de dicho valor recibido.

print("--------------------------------")
print("-------TABLA DE MULTIPLICAR-----")
print("--------------------------------")

# DEFINICIÓM DE LA FUNCIÓN 
def tabla_multiplicar(valor):
    for i in range(1, 11):
        print(f"{valor} x {i} = {valor * i}")

# INPUT 
valor = int(input("Mostrar tabla de el número: "))

# PROCESS AND OUTPUT 
print("Tabla de multiplicar del " + str(valor))

tabla_multiplicar(valor)
