numeros = [] # Crear una lista vacía para los números

# ciclo para ingresar los números
while True:
    i = input("Ingrese un número (o 'fin' para terminar): ") 
    if i.lower() == 'fin':
        break 
    numeros.append(int(i)) 

resultado = 0 

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
