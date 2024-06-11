#los errores de excepciones en un lenguaje de programacion no es otra cosa que los errores en tiempo de ejecucion
#Cuando se manejan los errores mediante las excepciones en realidad se dice que evita que se presenten esos errores
#en progra,a en tiempo ejecucion\

#Ejemplo se presenta un error cuando no es generada una variable
#try:
#  nombre=input("dame el nombre completo de una persona: ")
#
#  if len(nombre)>0:
#    nombre_usuario = "El nombre del usuario del sistema es: "+nombre  
#    
#  print(nombre_usuario)
#except:
#  print("es necesario introducir el nombre de la persona")

#Ejemplo 2: Cuando se solicita un numero y se ingresa otra cosa
try:
 numero=int(input("ingresa un numero entero: "))

 if numero>0:
    print("ingreso un numero entero")
 else:
    print("Ingreso un numero negativo") 
except ValueError:
  print("No es posible convertir una letra a un numero, Verifica porfavor...")

#cuando se generan multiples excepciones
try:
 numero=int(input("ingresa un numero: "))

 print("el Cuadrado del numero es: "+str(numero*numero))

except TypeError:
  print("Es Necesario convertir el numero a entero")

except ValueError:
  print("No es posible convertir una letra a un numero, varifica por favor..")
else:
    print("Todo se Ejecuto si errores")
finally:
    print("Ya acabo el codigo")
