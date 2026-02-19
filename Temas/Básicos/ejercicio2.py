import math

#Lectura de datos
def leerDatos():
  n= int(input("n: "))
  return n
#Proceso de datos
def calcularFn(n):
  
  aprox= math.sqrt(2*math.pi) *math.exp(-n)*n**(n+1/2)
  return aprox
#Mostrar resultados
def mostrarResultado(aprox):
  print("aproximación= ", aprox)

def ejercicio_2():
    #Bloque de código principal
    #llamada a las funciones
    n= leerDatos()
    aprox= calcularFn(n)
    mostrarResultado(aprox)
    