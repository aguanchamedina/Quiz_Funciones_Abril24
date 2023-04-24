# Construir una función que reciba un valor entero como parámetro y que determine si su último dígito es 4.

print("--------------------------------")
print("-------- ULTIMO DIGITO 4 -------")
print("--------------------------------")

# DEFINICIÓN DE LA FUNCIÓN 
def ultimo_digito_es_cuatro(valor):
    ultimo_digito = valor % 10
    if ultimo_digito == 4:
        return True
    else:
        return False

# INPUT
resultado = ultimo_digito_es_cuatro(int(input("Digite el número: ")))

if resultado:
    print("El último dígito es 4.") # OUTPUT
else:
    print("El último dígito no es 4.") # OUTPUT
