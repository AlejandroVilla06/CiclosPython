print("**** Fiesta bestia ****")
print(" ********** ")

print("0. Salir")
print("1. Registrar invitado")
print("2. Ver lista de invitados")
print("3. Ver invitados VIP")
print("4. Cobranza")
print("5. Editar informacion")
print("6. Retirar invitados")
print(" ********* ")

opcion = 90
usuarios=[]
while opcion != 0:
    invitado={}
    
    opcion=int(input("Digita una opcion: "))
    if opcion==1:
        invitado["nombre"]=input("Ingrese su nombre: ")
        invitado["id"]=int(input("Ingrese su id: "))
        invitado["cedula"]=input("ingrese su cedula: ")
        invitado["eps"]=input("Ingrese su eps: ")
        invitado["estado"]= bool(input("ya pago?: "))
        invitado["valorcuota"]=float(input("Ingrese la cuota: "))
        invitado["edad"]=input("Ingrese su edad: ")
        usuarios.append(invitado)
    elif opcion==2:
        #Recorriendo una lista
        for persona in usuarios:
            print(f"Persona:{persona['nombre']}")
            print(f"Id:{persona['id']}")
            print(f"Cedula:{persona['cedula']}")
            print(f"Eps: {persona['eps']}")
            print(f"Estado: {persona['estado']}")
            print(f"Valor Cuota: {persona['valorcuota']}")
            print(f"Edad:{persona['edad']}")
            
    elif opcion==3:
        for persona in usuarios:
            if persona["estado"]==True:
                print(persona)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion==6:
        pass
    else:
        print("Opcion invalida")
        