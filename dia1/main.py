productos = list()
ventas = list()

def mostrar_menu():
    """Menu Principal de la Aplicacion
    """
    print("\n====BODEGA====")
    print("1.-Registrar producto")
    print("2.-Listar productos")
    print("3.-Salir")

def main():
    mostrar_menu()
    while True:
        opcion = input("Opcion:")    
        if opcion == "1" : registrar()
        elif opcion == "2" :listar()
        elif opcion =="3": break
        else:print("Opcion Invalida")

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

if __name__ =="__main__":main()        