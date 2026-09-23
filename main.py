PRODUCTOS = [];

while True:
    print(f"\n{"MENÚ":*^30}")
    print(f"{'1. Agregar producto':^30}")
    print(f"{'2. Mostrar productos':^30}")
    print(f"{'3. Eliminar producto':^30}")
    print(f"{'4. Buscar producto':^30}")
    print(f"{'5. Salir':^30}")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        PRODUCTOS.append([nombre, categoria, precio])
        print(f"Producto '{nombre}' agregado exitosamente.")
        continue

    elif opcion == "2":
        if len(PRODUCTOS) == 0:
            print("No hay productos registrados.")
        else:
            print(f"\n{'LISTA DE PRODUCTOS':*^30}")
            for i, producto in enumerate(PRODUCTOS):
                print(f"({i+1}) Nombre: {PRODUCTOS[i][0]} // Categoría: {PRODUCTOS[i][1]} //Precio: ${PRODUCTOS[i][2]:.2f}")
        continue

    elif opcion == "3":
        if len(PRODUCTOS) == 0:
            print("No hay productos registrados.")
        else:
            print(f"\n{'LISTA DE PRODUCTOS':*^30}")
            for i, producto in enumerate(PRODUCTOS):
                print(f"({i+1}) Nombre: {PRODUCTOS[i][0]} // Categoría: {PRODUCTOS[i][1]} //Precio: ${PRODUCTOS[i][2]:.2f}")
            eliminar = int(input("Ingrese el número del producto que desea eliminar: "))
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
                    print(f"Producto encontrado: Nombre: {PRODUCTOS[i][0]} // Categoría: {PRODUCTOS[i][1]} //Precio: ${PRODUCTOS[i][2]:.2f}")
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró el producto '{buscar}'.")
        continue


    else:
        print("Saliendo del programa...")
        break