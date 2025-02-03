def operaciones(lista:list)->float:
    i=0
    sumatoria=0
    for i in range(len(lista)):
        sumatoria = lista[i]+sumatoria
        promedio = sumatoria/len(lista)
        i+=1
    retorno = print(f'La sumatoria es: {sumatoria} y El promedio es : {promedio}')
    return retorno

#Datos de entrada: 
#Longitud de la lista

lon_lista = int(input("Ingrese la longitud de la lista: "))

lista = []
i =0

for i in range(lon_lista):
    indicador_lis = float(input('ingrese el valor de la posicion {i} de la lista: '))
    lista.append(indicador_lis)
    i+=1

operaciones(lista)
minimo = min(lista)
maximo = max(lista)

print(f'El minimo es : {minimo}')
print(f'El maximo es: {maximo}')
