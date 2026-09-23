PRODUCTOS = [];

while True:
    print(f"\n{"MENÚ":*^30}")
    print(f"{'1. Agregar producto':^30}")
    print(f"{'2. Mostrar productos':^30}")
    print(f"{'3. Eliminar producto':^30}")
    print(f"{'4. Buscar producto':^30}")
    print(f"{'5. Modificar producto':^30}")
    print(f"{'6. Salir':^30}")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            nombre = input("Ingrese el nombre del producto: ")
            if not nombre:
                print("El nombre del producto no puede estar vacío.")
                continue
            categoria = input("Ingrese la categoría del producto: ")
            if not categoria:
                print("La categoría del producto no puede estar vacía.")
                continue
            precio = input("Ingrese el precio del producto: ")
            if not precio.isdigit():
                print("El precio del producto debe ser un número entero.")
                continue
            precio = int(precio)
            PRODUCTOS.append([nombre, categoria, precio])
            print(f"Producto '{nombre}' agregado exitosamente.")
            pregunta = input("¿Desea agregar otro producto? (s/n): ")
            if pregunta.lower() == "s":
                continue
            else:
                break

    elif opcion == "2":
        if len(PRODUCTOS) == 0:
            print("No hay productos registrados.")
        else:
            print(f"\n{'LISTA DE PRODUCTOS':*^30}")
            for i, producto in enumerate(PRODUCTOS):
                print(f"({i+1}) Nombre: {producto[0]} // Categoría: {producto[1]} // Precio: ${producto[2]}.00")
        continue

    elif opcion == "3":
        if len(PRODUCTOS) == 0:
            print("No hay productos registrados.")
        else:
            print(f"\n{'LISTA DE PRODUCTOS':*^30}")
            for i, producto in enumerate(PRODUCTOS):
                print(f"({i+1}) Nombre: {producto[0]} // Categoría: {producto[1]} //  Precio: ${producto[2]}.00")
            eliminar = input("Ingrese el número del producto que desea eliminar: ")
            if not eliminar.isdigit():
                print("Debe ingresar un número entero.")
                continue
            eliminar = int(eliminar)
            if eliminar < 1 or eliminar > len(PRODUCTOS):
                print("Número de producto inválido.")
            else:
                eliminado = PRODUCTOS.pop(eliminar - 1)
                print(f"Producto '{eliminado[0]}' eliminado exitosamente.")
        continue

    elif opcion == "4":
        if len(PRODUCTOS) == 0:
            print("No hay productos registrados.")
        else:
            buscar = input("Ingrese el nombre del producto que desea buscar: ")
            encontrado = False
            for i, producto in enumerate(PRODUCTOS):
                if producto[0].lower() == buscar.lower():
                    print(f"Producto encontrado: Nombre: {producto[0]} // Categoría: {producto[1]} // Precio: ${producto[2]}.00")
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró el producto '{buscar}'.")
        continue

    elif opcion == "5":
        if len(PRODUCTOS) == 0:
            print("No hay productos registrados.")
        else:
            print(f"\n{'LISTA DE PRODUCTOS':*^30}")
            for i, producto in enumerate(PRODUCTOS):
                print(f"({i+1}) Nombre: {producto[0]} // Categoría: {producto[1]} // Precio: ${producto[2]}.00")
            modificar = input("Ingrese el número del producto que desea modificar: ")
            if not modificar.isdigit():
                print("Debe ingresar un número entero.")
                continue
            modificar = int(modificar)
            if modificar < 1 or modificar > len(PRODUCTOS):
                print("Número de producto inválido.")
            else:
                while True:
                    print("Modificar:")
                    print("1. Nombre")
                    print("2. Categoría")
                    print("3. Precio")
                    seleccion = input("Ingrese la modificación que desea realizar: ")
                    if seleccion == "1":
                        nombre = input("Ingrese el nuevo nombre del producto: ")
                        if not nombre:
                            print("El nombre del producto no puede estar vacío.")
                            continue
                        PRODUCTOS[modificar - 1][0] = nombre
                        print(f"Nombre del producto modificado exitosamente a '{nombre}'.")
                        break
                    elif seleccion == "2":
                        categoria = input("Ingrese la nueva categoría del producto: ")
                        if not categoria:
                            print("La categoría del producto no puede estar vacía.")
                            continue
                        PRODUCTOS[modificar - 1][1] = categoria
                        print(f"Categoría del producto modificada exitosamente a '{categoria}'.")
                        break
                    elif seleccion == "3":
                        precio = input("Ingrese el nuevo precio del producto: ")
                        if not precio.isdigit():
                            print("El precio del producto debe ser un número entero.")
                            continue
                        precio = int(precio)
                        PRODUCTOS[modificar - 1][2] = precio
                        print(f"Precio del producto modificado exitosamente a ${precio}.00.")
                        break
                    else:
                        print("Opción inválida. Por favor, seleccione una opción válida.")
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")