def calcular_devuelta(valor_a_pagar:float,pago:float) -> float:
    devuelta = valor_a_pagar - pago
    return devuelta

#Datos de entrada
#input Nombre, Cantidad de productos, Categoria del billete
#Ouputs Valor a pagar y Devuelta
nombre = input("Ingrese su nombre: ")
cantidad_prod = int(input("Ingrese la cantidad de productos que desea procesar: "))

i=0
sumatoria_productos = 0

for i in range (cantidad_prod):
    
    valor_del_producto = float(input(f'Ingrese el valor del producto #{i+1}: '))

    sumatoria_productos = sumatoria_productos + valor_del_producto

    i=i+1
    
print(f'el valor a pagar es: {sumatoria_productos}')
den_pago = float(input("Con que denominacion va a realizar el pago: "))

print(f'Su devuelta son: {calcular_devuelta(den_pago,sumatoria_productos)}$')

