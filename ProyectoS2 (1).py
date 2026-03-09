import json
import time 
try:
    with open("inventario.json", "r") as archivo:
        inventario = json.load(archivo)
except:
    inventario = [] 

print("Bienvenido al menu de herramientas")

while True:
    print(" Menu De Herramientas ")
    print("1. colocar una herramienta nueva")
    print("2. mostrar Todas las herramientas ")
    print("3. Buscar herramienta por nombre o Id")
    print("4. cambiar estado de herramienta")
    print("5. Herramienta para eliminar")
    print("6. SALIR ")
    
    opcion = input("Escojer una opcion ")

    if opcion == "1":
        print("Ingrese herramienta")
        id_h = input("ID: ")
        nombre = input("Nombre: ")
        cat = input("Categoría: ")
        cant = int(input("Cantidad: "))
        estado = "activa" 
        valor = input("Valor estimado: ")
        
        herramienta = {
            "id": id_h, 
            "nombre": nombre, 
            "categoria": cat, 
            "stock": cant, 
            "estado": estado, 
            "valor": valor
        }
        inventario.append(herramienta)
        
        with open("inventario.json", "w") as archivo:
            json.dump(inventario, archivo, indent=4)
        print("Herramienta guardada en la lista y en el archivo JSON")

    elif opcion == "2":
        print("lista de herramientas")
        if len(inventario) == 0:
            print("la lista está vacío")
        else:
            for h in inventario:
                print("..........................")
                print("ID =", h["id"])
                print("..........................")
                print("Nombre =", h["nombre"])
                print("..........................")
                print("Categoría =", h["categoria"])
                print("..........................")
                print("Stock =", h["stock"])
                print("..........................")
                print("Estado =", h["estado"])
                print("..........................")
                print("Valor =", h["valor"])
    
    elif opcion == "3":
        print("Herramienta que quiero Buscar")
        buscar = input("Escribe el Id de la herramienta que quieres")
        encontrado = False
        for h in inventario:
            if h["id"] == buscar:
                print("Herramienta encontrada:", h)
                encontrado = True
        if encontrado == False:
            print("No existe una herramienta con ese nombre o Id")

    elif opcion == "4":
        print("cambiar estado de Herramientas")
        id_modificar = input("Id de la herramienta que quiero cambiar ")
        for h in inventario:
            if h["id"] == id_modificar:
                print("Estado actual:", h["estado"])
                nuevo_estado = input("Eponer  el nuevo estado de la herramienta ")
                h["estado"] = nuevo_estado
            
                with open("inventario.json", "w") as archivo:
                    json.dump(inventario, archivo, indent=4)
                print("lista actualizada y guardada")

    elif opcion == "5":
        print(" eliminar la  Herramienta")
        id_eliminar = input("Id de la herramienta que quiero quitar ")
        for h in inventario:
            if h["id"] == id_eliminar:
                inventario.remove(h)

                with open("inventario.json", "w") as archivo:
                    json.dump(inventario, archivo, indent=4)
                print("Herramienta eliminada ")

    elif opcion == "6":
        print("Cerrando.... ")
        time.sleep(2)
        print("Salites del sistema, gracias por usar nuestro servicio")
        break

    else:
        print("Esa opción no existe, Pon un numero del 1 al 6")