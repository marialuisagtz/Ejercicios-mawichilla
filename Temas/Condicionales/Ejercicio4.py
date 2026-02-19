

def leerDatos():
  a= int(input("ingresa un numero para la a: "))
  b= int(input("ingresa un numero para la b: "))
  c= int(input("ingresa un numero para la c: "))
  return a,b,c

def analizarDatos(a,b,c):
  d= b**2 - 4 * a * c
  if d > 0:
    mensaje="la gráfica es una hipérbola"

  if d == 0:
    if a == 0 and c ==0:
      mensaje="la gáfica es una recta"
    else:
      mensaje="la gráfica es una parábola"
  if d < 0:
    if a == c:
      mensaje="la gráfica es una circunferencia"
    else:
      mensaje="la gráfica es una elipse"

  return mensaje
def mostrarMensaje(mensaje):
  print(mensaje)


def ejercicio_4():
    #llamada a las funciones
    a,b,c= leerDatos()
    mensaje= analizarDatos(a,b,c)
    mostrarMensaje(mensaje)