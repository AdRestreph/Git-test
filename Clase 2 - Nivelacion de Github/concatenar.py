def concatenar_Lista(lista:list)->str:
    i=0
    concatena =""
    for i in range(len(lista)):
        concatena = concatena + lista[i]
        i+=1

    return concatena

tamano_lista = int(input("Ingrese el tamaño que desea en la lista: "))
lista = []

for i in range(tamano_lista):
    elemento = input(f'Ingrese el valor que desea en la posicion [{i}]:  ')
    lista.append(elemento)
    i+=1

print(f'Esta es la concatenacion:  {concatenar_Lista(lista)}')
