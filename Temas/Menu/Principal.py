from Temas.Básicos.ejercicio1 import ejercicio_1
from Temas.Básicos.ejercicio2 import ejercicio_2
from Temas.Listas.Ejercicio3 import ejercicio_3
from Temas.Condicionales.Ejercicio4 import ejercicio_4
from Temas.Ciclos.Ejercicio5 import ejercicio_5
    #carpeta.carpeta.archivo        funcion
from Temas.poo.clases.ejer1poo import Ejercicio1
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
                ejercicio_2()
                print()  
            case 3:
                ejercicio_3()
                print()  
            case 4:
                ejercicio_4()
                print()
            case 5:
                ejercicio_5()
                print()
            case 6:
                print("Hasta pronto")
                break
            case _:
                print("Opción no válida")
            
                
    
        
     
    
