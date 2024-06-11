#crear un programa que calcule y obtenga el total a pagar de un producto determinado. 
#se debera de solicitar el nombre y descripcion del producto, codigo de producto, cantidad del producto, precio unitario del producto.
#el total a pagar incluye el iva y el descuento.
#si se compran de 1 a 5 productos se otroga el 10% de descuento, sise compran de 6 a 10 el 15%, si se compran mas de 10 el 20% 

prod = str(input("Ingresa el nombre del producto: "))
#descrip = str(input("Ingresa una descripcion del producto: "))
#cod = str(input("Ingresa el codigo del producto: "))
cant = int(input("Ingrese la cantidad del producto: "))
precio = float(input("Ingrese el precio unitario del producto: "))


if cant >= 1 and cant <= 5:
    descuento = 0.1
elif cant >= 6 and cant <= 10:
    descuento = 0.15
else:
    descuento = 0.2

sub = cant * precio
iva = sub * 0.16
sub2 = sub + iva
desc = sub2 * descuento
total = sub2 - desc

print (f"el precio unitario de {prod} es de {precio} \nse esta comprando una cantidad de {cant} \nel subtotal seria de {sub} \ny el precio contando iva y descuento es de {total}")



