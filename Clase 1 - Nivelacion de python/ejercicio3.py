def Mayor_de_edad(edad:int)->bool:
    i = False
    if edad >= 18:
        i=True
    return i
#Datos de entrada:
#Nombre,Apellido, edad
adultos = []

for i in range(3):
    edad=int(input("Ingrese su edad: "))
    if edad <= 5:
        print("Primera infancia")
    elif 6 <= edad <= 12:
        print("Niñez")
    elif 13 <= edad <= 17:
        print("Adolecencia")
    else:
        print("Mayor de edad")
        nombre=input("ingrese su nombre: ")
        apellido=input("ingrese su Apellido: ")
        adultos.append({"Nombre":nombre,"Apellido":apellido,"Edad":edad})
    i+=1

print(adultos)



