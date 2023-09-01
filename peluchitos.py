peluches=["roshi","conejito","aguacatico"]

opcion=0
print("Pelucheria PELUCHITOS")
print("..............")
print("1. Agregar producto a la bodega")
print("2. Ver productos en bodega")
print("3. Obtener valor del inventario")
print("4. Ver productos mas vendidos")
print("5. SALIR")

while(opcion!=5):
    opcion=int(input("Digita un numero: ")) 
    
    if opcion==1:
        nombre=input("Digita el nombre del producto: ")
        #agregando una lista o arreglo
        peluches.append(nombre)
        print("Peluche agregado correctamente.....")
    elif opcion==2:
        print(peluches)
    elif opcion==3:
        print("Usted esta en la opcion 3")
    elif opcion==4:
        print("Usted esta en la opcion 4")
    else:
        print("La opcion no existe")
    
                  
print("Sali del ciclo")
    
