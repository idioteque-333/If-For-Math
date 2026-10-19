import math  # Librería matemática  

# Programa que solicita nombre y precio de un producto.
Productos = []  #Lista para guardar los nombres
Precios  = []  #Lista para guardar los precios 

# --- Entrada de Datos con Ciclo For ---
for i in range(5):
    Nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    try:
        Precio = float(input(f"Imgrese el precio de {Nombre}: "))
    except ValueError:
        print ("Error: Debes ingresar un número válido. ")
        Precio = 0.0 
    Productos.append(Nombre)
    Precios.append(Precio)

# --- Cálculos ---
Promedio = sum(Precios) / len(Precios)

# Usando math para redondear el promedio 
Promedio_Redondeado_Arriba = math.ceil(Promedio)
Promedio_Redondeado_Abajo = math.floor(Promedio)

# Producto con precio mínimo y máximo
Precio_Min = min(Precios)
Precio_Max = max(Precios)
Producto_Min = Productos[Precios.index(Precio_Min)]
Producto_Max = Productos[Precios.index(Precio_Max)]

# --- Resultados ---
print ("\n === RESULTADOS ===")
print (f"Promedio de Precios: {Promedio:.2f}")
print (f"Promedio redondeado hacia arriba: {Promedio_Redondeado_Arriba}")
print (f"Promedio redondeado hacia abajo: {Promedio_Redondeado_Abajo}")
print (f"Producto más barato: {Producto_Min} (${Precio_Min:.2f})")
print (f"Producto más caro: {Producto_Max} (${Precio_Max})")

# Verificar si algún producto tiene precio menor al promedio 
print ("\n Productos con precio menor al promedio")
Hay_Menor = False
for i in range(len(Productos)):
    if Precios [i] < Promedio:
        print (f" - {Productos[i]} (${Precios[i]:.2f})")
        Hay_Menor = True 

if not Hay_Menor:
    print ("Ningún producto tiene precio menor al promedio")