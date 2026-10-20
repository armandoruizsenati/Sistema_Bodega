productos = list()
ventas = list()


def mostrar_menu():
    print("\n========== BODEGA ==========")
    print("1.- Registrar producto")
    print("2.- Listar productos")
    print("3.- Modificar producto")
    print("4.- Eliminar producto")
    print("5.- Ventas")
    print("6.- Listar Ventas")
    print("7.- Salir")
    print("============================")

def main():
    while True:
        mostrar_menu()  # Mostrar antes de elegir
        opcion = input("Seleccione una opción (1-7): ")
        if opcion == "1":registrar()
        elif opcion == "2":listar()
        elif opcion == "3":modificar()
        elif opcion == "4":eliminar()
        elif opcion == "5":VentasBodega()
        elif opcion == "6":listar_ventas()
        elif opcion == "7":
            print("Gracias por utilizar BODEGA")
            break
        else:
            print("Opción inválida")
            continue
        continuar = input("\n¿Desea continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Gracias por utilizar BODEGA")
            break   

def leer_entero(mensaje,minimo=0):
    """Funcion que me permite validar numeros enteros
    Descripcion: Se ingresar numeros mayores a cero
    Parametros:Numero a evaluar {mensaje}
    Retorna numero valido si es mayor a cero
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= minimo:return valor
        except ValueError:pass
        print(f"Ingrese un entero mayor o igual a {minimo}")    


def leer_precio(mensaje):
    while True:
        try:
            valor = float(input(mensaje).replace(",","."))
            if valor > 0: return round(valor,2)
        except ValueError: pass
        print("Ingrese un precio valido mayor que cero")    

def buscar(codigo):
    return next((p for p in productos if p["codigo"]==codigo),None)

def registrar():
    codigo = input("Codigo:").strip().upper()
    if not codigo or buscar(codigo):
        print("Codigo vacio o repetido")
        return
    nombre = input("Nombre:").strip()
    if not nombre:
        print("Nombre es obligatorio")
        return
    precio = leer_precio("Precio S/:")
    stock =leer_entero("Stock Inicial:")
    productos.append(
        {
          "codigo":codigo,
          "nombre":nombre,
          "precio":precio,
          "stock":stock }
          )
def listar():
    if not productos:
        print("No Hay productos que mostrar")    
        return
    for p in productos:
        print(f"{p["codigo"]:8} {p["nombre"]:20} \n"
              f"S/.{p["precio"]:8.2f} Stock: {p["stock"]}")

def modificar():
    p = buscar(input("Codigo a Modificar:").strip().upper())
    if not p:
        print("No Encontrado el producto")
        return  
    nuevo_nombre = input(f"Nuevo Nombre para {p["nombre"]}:")      
    p["nombre"] = nuevo_nombre
    p["precio"] =leer_precio("Nuevo Precio S/.")
    print("Producto Actualizado")

def eliminar():
    p = buscar(input("Codigo a eliminar:").strip().upper())
    if not p:  
        print("No Encontrado")  
        return
    if input("Confirmar eliminacion: (s/n):").lower()=="s":
        productos.remove(p)
        print("Producto Eliminado")

def VentasBodega():
    venta = input("Numero Venta:")
    cliente = input("Nombre Del Cliente:")
    producto = input("Codigo Producto:")
    cantidad = input("Cantidad Producto:")
    ventas.append(
        {
          "codigo":venta,
          "cliente":cliente,
          "producto":producto,
          "cantidad":cantidad }
          )
def listar_ventas():
    if not ventas:
        print("No Hay Ventas que mostrar")    
        return
    for v in ventas:
        print(f" Venta : {v["codigo"]:8} Cliente : {v["cliente"]:20} \n"
              f" Producto : {v["producto"]:8} Cantidad: {v["cantidad"]}")    

if __name__ =="__main__":main()        