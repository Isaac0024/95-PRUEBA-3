def mostrar_escenario(escenario):
    print("\t\t\t ESCENARIO\n")#\t tabulador
    for contador_fila in range(0, 50, 10):
        fila = ""#inicializando
        for contador_columna in range(10):
            fila += f"{escenario[contador_fila + contador_columna]}\t"
        print(fila)
    print("\n")

def comprar_entradas(escenario):
    precios = {i: 10000000 for i in range(1, 21)}
    precios.update({i: 1000000 for i in range(21, 31)})
    precios.update({i: 950000 for i in range(31, 51)})

    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1 o 2): "))
    if cantidad < 1 or cantidad > 2:
        print("Cantidad inválida.")
        return
    for _ in range(cantidad):
        mostrar_escenario(escenario)
        asiento = int(input("Seleccione el número del asiento que desea comprar: "))
        if escenario[asiento - 1] == 'X':
            print("El asiento no está disponible.")
            return
        escenario[asiento - 1] = 'X'
        precio = precios[asiento]
        run = input("Ingrese el RUN de la persona que ocupará el asiento (sin guión ni puntos): ")
        compradores.append((asiento, precio, run))
        print(f"Se ha comprado el asiento {asiento} por ${precio} para el RUN {run}.\n")

escenario = []
compradores = []
for i in range(1, 51):
    escenario.append(str(i))
try:  
    while True:
        print("1. Comprar entradas")
        print("2. Mostrar ubicaciones disponibles")
        print("3. Mostrar ganancias")
        print("4. Mostrar compradores")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == "1":
            comprar_entradas(escenario)
        elif opcion == "2":
            mostrar_escenario(escenario)
        elif opcion == "3":
            ganancia_total = sum(venta[1] for venta in compradores)
            print(f"Ganancias totales: ${ganancia_total}")
            print()
        elif opcion == "4":
            print("RUN de personas que compraron entradas: ")
            for venta in compradores:
                print(f"RUN: {venta[2]}")
                print()
        elif opcion == "5":
            print("Salio de operación")
            break
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.\n")
except ValueError:
    print("Ha ocurrido un error en el sistema")
