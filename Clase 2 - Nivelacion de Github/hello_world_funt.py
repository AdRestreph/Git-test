def Hello_world(nombre:str)->str:
    saludo = print(f'Hello world im {nombre}!')
    return saludo

ingreso = input("Ingresa tu nombre: ")
Hello_world(ingreso)