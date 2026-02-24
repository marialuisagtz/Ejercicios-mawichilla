
from Temas.Básicos.ejercicio1 import ejercicio_1
from Temas.Básicos.ejercicio2 import ejercicio_2
from Temas.Listas.Ejercicio3 import ejercicio_3
from Temas.Condicionales.Ejercicio4 import ejercicio_4
from Temas.Ciclos.Ejercicio5 import ejercicio_5
    #carpeta.carpeta.archivo        funcion
from Temas.poo.clases.ejer1poo import Ejercicio1
from Temas.poo.clases.ejer2poo import Ejercicio2
from Temas.poo.clases.ejer3poo import Ejercicio3
from Temas.poo.clases.ejer4poo import Ejercicio4
from Temas.poo.clases.ejer5poo import Ejercicio5
# carpetas           archivo           clase 
def menuPrincipal():
    while True:
        print(" \n\n : : Menú principal")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Salir")
        
        op= int(input("Elija la opción deseada: "))
        print()
        match(op):
            case 1:
                #ejercico_1
                #cerear el objeto de la clase 
                e1= Ejercicio1()
                e1.leerDatos()
                e1.calcularX()
                e1.mostrarResultado()
                print()
                ejercicio_1()
                print()
            case 2:
               e2= Ejercicio2()
               e2.leerDatos()
               e2.calcularFn()
               e2.mostrarResultado()
               print()  
            case 3:
                e3= Ejercicio3()
                e3.mostrarIndices()
                print()  
            case 4:
               e4= Ejercicio4()
               e4.leerDatos()
               e4.analizarDatos()
               e4.mostrarMensaje()
               print()
            case 5:
               e5= Ejercicio5()
               e5.leerDatos()
               e5.calcularAprox()
               e5.mostrarResultados()
                
               print()
            case 6:
                print("Hasta pronto")
                break
            case _:
                print("Opción no válida")
            
                
    
        
     
    
