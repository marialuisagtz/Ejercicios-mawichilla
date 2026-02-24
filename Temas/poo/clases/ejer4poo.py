
class Ejercicio4():
    def __init__(self):
        
        self.a=0
        self.b=0
        self.c=0
        self.mensaje= ""
    def leerDatos(self):
        self.a = int(input("ingresa un numero para la a: "))
        self.b = int(input("ingresa un numero para la b: "))
        self.c = int(input("ingresa un numero para la c: "))
    

    def analizarDatos(self):
        d= self.b**2 - 4 * self.a * self.c
        if d > 0:
            self.mensaje="la gráfica es una hipérbola"

        if d == 0:
            if self.a == 0 and self.c ==0:
                self.mensaje="la gáfica es una recta"
            else:
                self.mensaje="la gráfica es una parábola"
        if d < 0:
            if self.a == self.c:
                self.mensaje="la gráfica es una circunferencia"
            else:
                self.mensaje="la gráfica es una elipse"

        
    def mostrarMensaje(self):
        print(self.mensaje)

