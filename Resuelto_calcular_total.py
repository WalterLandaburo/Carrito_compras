#Aplicar docstring en las funciones
#Aplicar funciones para descomponer en partes 
#Aplicar try-except para manejar errores con los datos ingresados
#Aplicar importar módulo estándar datetime al agregar un producto al carrito 🛒 
#Usar una función para calcular la cantidad del producto elegido por su precio 
#Usar una función para mostrar el total a pagar 


#Para la función calcular_total estaba usando dos nombres similares: 'sumar' y 'suma', lo que genero me equivoque imprimiendo la lista que contenía los precios a sumar, en vez de la variable que contenía el valor total 


#Lista principal donde se almacenan los productos
productos = []

precios = []
#Módulo datetime 
from datetime import datetime


#Funciones

def fecha_hora_accion():
    fecha_hora = datetime.now()

    print(fecha_hora.strftime("%d de %B de %Y"))


def agregar_producto():
            
  #agregar producto: nombre, precio 
        
 
    #nombre           
            nombre = input("\nIngresá el nombre del producto (sólo letras):").strip().lower()
                
            if nombre.isdigit() or nombre == "":
                print("\nDato no válido.")
                 
            if nombre not in productos:
        
        #precio          
                precio = input("\nIngresá el precio del producto (sólo números enteros positivos): $").strip()
                
                if precio.isdigit() and int(precio) >= 0 and precio != "":
                    #TRABAJAR CON SUB-LISTA
                    producto = [nombre, precio]
                    
                    #AÑADIR A LISTA PRINCIPAL 
                    productos.append(producto)
                    
                    #AÑADIR A LISTA PARA CALCULAR IMPORTE TOTAL 
                    precios = []
                    precios.append(precio)
                    
                    #Limpiar sub-lista
                    #producto.clear()
                    
                     
                
                else:
                           
                    print("\nDato no válido")
                    
    
    
def mostrar_productos():
    
    if productos:
        #Ordenar lista 
        productos.sort()
        print("\n\n---Lista de productos actualizada---")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre del producto: {producto[0]}.  Precio: ${producto[1]}\n")
            
    else:
        print("La lista de productos está vacía.")
                       
    
         
        
        
        
        
def borrar_producto():
    if len(productos) == 0:
        print("No hay productos ingresados.")
    
    if productos:
        
        mostrar_productos()
       
        
        number = input("número del producto a Eliminar:")
                
        if not number.isdigit():
            print("❌ Dato no válido.")
                     
                
        if not number:
            print("❌ Dato no válido.")
                          
                
        #se imprimen los productos numerados desde el 1, por eso se resta 1 al número seleccionado por el usuario, así va a coincidir con la posición (la posición inicia en cero)
        posicion_borrar = int(number) - 1
           
        #le di un nombre a la acción de borrar para usarla como orientación, así ubico con una posición en esta variable el nombre del producto para imprimirlo por pantalla 
        sublist_borrar = productos.pop(posicion_borrar)
                    
        print (f"El producto {sublist_borrar[0]} fue eliminado.\n")

def buscar_producto():
    
    if not productos:
        print("❌ No hay ningún producto en la lista para calcular el costo.")
        print("Ingrese la opción del menú para agregar un producto.")
    
    find = input("\nProducto que desea comprar: ").strip().lower()  
              
    if find.isdigit():
        print("❌ Dato no válido.")
                
    if find.isdigit():
        print("❌ Dato no válido.")

    for producto in productos:
        if producto[0] == find:
            print("🔍 Buscando ...")
            print("PRODUCTO ENCONTRADO")
            print(f"Nombre del producto: {producto[0].title()} Precio: ${producto[1]}")
            
def calcular_por_producto(price, cantidad):  
    
    
     
    importe = int(price) * int(cantidad)
    
    print(f"El total a pagar es ${importe}")
 

def calcular_total():   
    
    sumar = []
    
    #mostrar lista principal ordenada 
    if not productos:
        print("La lista de productos está vacía.")
    
    if productos:   
        #Ordenar lista 
        productos.sort()
        print("\n\n---Lista de productos actualizada---")
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. Nombre del producto: {producto[0]}.  Precio: ${producto[1]}\n")
            
        
            sumar.append(producto[1])
            
            
    suma = 0
    for number in sumar:
        suma += int(number)
                
        print(f"\n\n Cantidad de productos: {len(productos)}")
            
        print(f"🛒 Importe total del carrito: ${suma}")
                
                 
            
            
    
        
                       
    
    
      
             
    
            
            
def mostrar_menu():  
    bucle = True                            
    while bucle == True:
         print("Menú de gestión compra 🛒:")
         print("1. Agregar un producto")
         print("2. Consultar la lista de productos")
         print("3. Borrar un producto")
         print("4. Importe total por producto")
         print("5. Total a pagar")
         print("6. Salir")
         
         opcion = input("Elige una opción del 1 al 6: ").strip()
         
         if opcion.isdigit():
             if 0 < int(opcion) <7:
                 
                 if int(opcion) == 1:
                   producto = agregar_producto()
                   print("\n\n")
                   tiempo= fecha_hora_accion()
                   print("PRODUCTO AGREGADO")
                   
                   
                   print("\n\n---Lista de productos actualizada---")
                   for i, producto in enumerate(productos, start=1):
                       print(f"{i}. Nombre del producto: {producto[0]}.  Precio: ${producto[1]}\n")
            
                 
                 elif int(opcion) == 2:
                   print("\n\n")
                   tiempo= fecha_hora_accion()
                   lista = mostrar_productos()
                   print("\n\n")
                   
                 elif int(opcion) == 3:
                   print("\n\n")
                   tiempo= fecha_hora_accion()
                   producto_eliminado = borrar_producto()
                   print("\n\n")
                   
                 
                 elif int(opcion) == 4:
                   print("\n\n")
                   tiempo= fecha_hora_accion()
                   buscar_producto()
                   price = input("Ingrese el precio del producto: ").strip()
    
    
                   cantidad = input("Ingrese la cantidad que desea comprar: ").strip()              
                
                   calcular_por_producto(price, cantidad)
                   
                 elif int(opcion) == 5:
                   print("\n\n")
                   tiempo= fecha_hora_accion()   
                   calcular_total()
                   
                 elif int(opcion) == 6:
                   print("\n\n")
                   print("Gracias por usar el programa. Chau.")
                   tiempo = fecha_hora_accion()
                   bucle = False
         else: 
             print("Opción no válida. Por favor, ingrese un número del 1 al 4 (incluidos).\n")
             
mostrar_menu()                 


