import random
import string
ids = []
nombres = []
tipos = []
tokens = []
responsables = []
estados = []
fechas = []
descripciones = []
observaciones = []
#----------------------------------------#
#--|menu_principal_asignador_de_tokens|--#
#----------------------------------------#
while True:
    print("menu principal asignador de tokens")
    print("1) registrar elemento")
    print("2) editar elemento")
    print("3) eliminar elemento")
    print("4) buscar elemento")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #------------------------#
    #--|registrar_elemento|--#
    #------------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_elemento = 1
        else:
            id_elemento = ids[-1] + 1
        nombre = input("nombre: ")
        tipo = input("tipo: ")
        while True:
            token = "TKN-"
            for i in range(10):
                token += random.choice(string.ascii_uppercase + string.digits)
            if token not in tokens:
                break
        responsable = input("responsable: ")
        estado = input("estado (activo o inactivo): ")
        fecha = input("fecha de registro: ")
        descripcion = input("descripción: ")
        observacion = input("observación: ")
        ids.append(id_elemento)
        nombres.append(nombre)
        tipos.append(tipo)
        tokens.append(token)
        responsables.append(responsable)
        estados.append(estado)
        fechas.append(fecha)
        descripciones.append(descripcion)
        observaciones.append(observacion)
        print("elemento registrado correctamente.")
        print("id:", id_elemento)
        print("token generado:", token)
    #---------------------#
    #--|editar_elemento|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("editar elemento")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {tokens[i]}")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("token:", tokens[posicion])
                nombres[posicion] = input("nuevo nombre: ")
                tipos[posicion] = input("nuevo tipo: ")
                responsables[posicion] = input("nuevo responsable: ")
                estados[posicion] = input("nuevo estado: ")
                fechas[posicion] = input("nueva fecha: ")
                descripciones[posicion] = input("nueva descripción: ")
                observaciones[posicion] = input("nueva observación: ")
                print("el token no puede modificarse.")
                print("elemento actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_elemento|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("eliminar elemento")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {tokens[i]}")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del elemento")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("token:", tokens[posicion])
                respuesta = input("¿desea eliminar este elemento? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    tipos.pop(posicion)
                    tokens.pop(posicion)
                    responsables.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    descripciones.pop(posicion)
                    observaciones.pop(posicion)
                    print("elemento eliminado correctamente.")
                else:
                    print("el elemento no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_elemento|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            print("buscar elemento")
            id_buscar = int(input("ingrese la id del elemento: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("tipo:", tipos[posicion])
                print("token:", tokens[posicion])
                print("responsable:", responsables[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print("descripción:", descripciones[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen elementos registrados.")
        else:
            activos = 0
            inactivos = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {tokens[i]} | {estados[i]}")
                if estados[i].lower() == "activo":
                    activos += 1
                elif estados[i].lower() == "inactivo":
                    inactivos += 1
            print("estadísticas asignador de tokens")
            print("cantidad de registros:", len(ids))
            print("activos:", activos)
            print("inactivos:", inactivos)
            print("tokens generados:", len(tokens))
            posicion = random.randint(0, len(ids) - 1)
            print("registro seleccionado")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("tipo:", tipos[posicion])
            print("token:", tokens[posicion])
            print("responsable:", responsables[posicion])
            print("estado:", estados[posicion])
            print("fecha:", fechas[posicion])
            print("descripción:", descripciones[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el asignador de tokens.")
        break
    else:
        print("opción no válida.")