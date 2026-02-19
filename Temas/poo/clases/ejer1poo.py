import math
class Ejercicio1():
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        
    def leerDatos():
        self.a = int(input("a: "))
        self.b = int(input("b: "))
        self.c = int(input("c: "))
        
    
    def calcularX(self):
        x= (math.sqrt(self.b-self.a**2)) / (self.c)
        
        #Mostrar resultados
        def mostrarResultado(x):
        print("x= ",self.x)    
    