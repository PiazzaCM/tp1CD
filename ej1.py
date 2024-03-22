#Crear una función que dado un número "n" calcular su factorial sin utilizar el operador "*"
 

def multiplicacion(a, b):
    resultado = 0
    for _ in range(b):
        resultado = resultado+a
    return resultado

def factorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado = multiplicacion(resultado, i)
    return resultado

num = int(input("Ingresa un número para calcular su factorial: "))
resultado = factorial(num)
print("El factorial de", num, "es", resultado)
#factorial es la funcion para calcular el factorial
#range es el rango de numeros
