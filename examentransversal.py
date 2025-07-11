productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
}

stock = {
    '8475HD':   [387990, 10],
    '2175HD':   [327990, 4],
    'JjfFHD':   [424990, 1],
    'fgdxFHD':  [664990, 21],
    '123FHD':   [290890, 32],
    '342FHD':   [444990, 7],
    'GF75HD':   [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}
def stock_marca(marca):
    buscada = marca.lower()
    total = sum(
        stock.get(modelo, [0, 0])[1]
        for modelo, datos in productos.items()
        if datos[0].lower() == buscada
    )
    print(f"El stock es: {total}")

def busqueda_precio(p_min, p_max):
    resultados = [
        f"{productos[modelo][0]}--{modelo}"
        for modelo, (precio, cantidad) in stock.items()
        if cantidad > 0 and p_min <= precio <= p_max
    ]
    resultados.sort()
    if resultados:
        print(f"Los notebooks entre los precios consultas son: {resultados}")
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        return True
    return False

def examen():
    estado = True
    while estado:
        print('***  MENÚ PRINCIPAL  ***')
        print("1. Stock marca.")
        print("2. Busqueda por precio.")
        print("3. Actualizar por precio.")
        print("4. Salir.")
        opcion = input('Seleccione una opción: ').strip()

        if opcion == '1':
            marca = input('Ingrese marca a consultar: ')
            stock_marca(marca)

        elif opcion == '2':
            while True:
                try:
                    p_min = int(input('Ingrese precio mínimo: '))
                    p_max = int(input('Ingrese precio maximo: '))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_precio(p_min, p_max)

        elif opcion == '3':
            repetir = 'si'
            while repetir == 'si':
                modelo = input('Ingrese modelo a actualizar: ').strip()
                try: 
                    nuevo_precio = int(input('Ingrese precio nuevo: '))
                except ValueError:
                    print("Debe ingresar un número entero para el precio.")
                    continue

                if actualizar_precio(modelo, nuevo_precio):
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")

                repetir = input("¿Desea actualizar otro precio de notebook? (si/no): ").strip().lower()

        elif opcion == '4':
            print('Programa finalizado')
            estado = False

        else:
            print('Opcion invalida. Por favor ingrese 1, 2 ,3 o 4.')
                
if __name__ == '__main__':
    examen()