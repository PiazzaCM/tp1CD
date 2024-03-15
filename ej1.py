#Crear una función que dado un número "n" calcular su factorial sin utilizar el operador "*"
def suma(a, b):
    return a + b   

def multiplicacion(a, b):
    resultado = 0
    for _ in range(b):
        resultado = suma(resultado, a)
    return resultado

def factorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado = multiplicacion(resultado, i)
        return resultado

num = int(input("Ingresa un número para calcular su factorial: "))
resultado = factorial(num)
print("El factorial de", num, "es", resultado)
