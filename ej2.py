numeros = [] # Crear una lista vacía para los números


num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

resultado = 0 

numeros.append(int(num1))
numeros.append(int(num2))

# ciclo para sumar los números
for i in numeros: 
    resultado -= -i  
print("La suma de los números es:", resultado) 


#append agrega numeros a la lista
#lower convierte a minusculas
#break termina el ciclo
# -= resta negativa
# -num negativo
#int convierte a entero