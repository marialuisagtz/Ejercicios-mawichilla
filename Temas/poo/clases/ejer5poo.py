import math
class Ejercicio5():
    def __init__(self):
        self.x= 0
        self.tol= 0
        self.aprox= 0
        self.valorReal= 0
        self.error= 0
        self.k= 0
        
    def leerDatos(self):
     self.x= float(input("Ingresa el valor de x: "))
     self.tol= float(input("Ingresa el valor de la tolerancia: "))
    

    def calcularAprox(self):
      self.k= 0
      self.aprox= 0
      self.valorReal= math.atan(self.x)
      self.error= self.tol + 1

      while self.error > self.tol:
            self.aprox += (-1)**self.k * (self.x**(2*self.k+1)) / (2*self.k+1)
            #aprox += (-1)**k*(x**(2*k+1)) / (x**(2*k+1))
            self.error= math.fabs((self.valorReal - self.aprox) / self.valorReal)*100
            self.k += 1
    

    def mostrarResultados(self):
        print("aprox=", self.aprox)
        print("valor real=", self.valorReal)
        print("error=", self.error)
        print("k=", self.k)

    