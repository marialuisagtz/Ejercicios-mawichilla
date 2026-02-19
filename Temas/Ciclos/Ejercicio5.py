#Solo comprendi la lectura
import math
def leerDatos():
  x= float(input("Ingresa el valor de x: "))
  tol= float(input("Ingresa el valor de la tolerancia: "))
  return x,tol

def calcularAprox(x,tol):
  k= 0
  aprox= 0
  valorReal= math.atan(x)
  error= tol + 1

  while error > tol:
    aprox += (-1)**k * (x**(2*k+1)) / (2*k+1)
    #aprox += (-1)**k*(x**(2*k+1)) / (x**(2*k+1))
    error= math.fabs((valorReal - aprox) / valorReal)*100
    k += 1
  return aprox, error, valorReal, k

def mostrarResultados(aprox, error, valorReal, k):
  print("aprox=", aprox)
  print("valor real=", valorReal)
  print("error=", error)
  print("k=", k)

def ejercicio_5():
    #Llamadas a las funciones
    x, tol= leerDatos()
    aprox, error, valorReal, k= calcularAprox(x, tol)
    mostrarResultados(aprox, error, valorReal, k)
 