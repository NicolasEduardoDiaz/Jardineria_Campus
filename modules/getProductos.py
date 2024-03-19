import os
import re
from tabulate import tabulate
import requests

# Devuelve un listado con todos los productos que pertenecen a la gama Ornamentales 
# y que tienen más de 100 unidades en stock. El listado deberá estar ordenado por su precio de venta, 
# mostrando en primer lugar los de mayor precio.
def getAllData():
    # json-server storage/producto.json -b 5501
    peticion = requests.get("http://172.16.102.108:5501/productos")
    data = peticion.json()
    return data

def getProductCodigo(codigo):
    peticion = requests.get(f"http://172.16.102.108:5501/productos/{codigo}")
    return [peticion.json()] if peticion.ok else []
    # if(peticion.ok):
    #     return [peticion.json()]
    # else:
    #     return []
   

def getAllStocksPriceGama(gama, stock):
    peticion = requests.get(f"http://154.38.171.54:5008/productos?gama={gama}&cantidadEnStock_gte={stock}&_sort=-precio_venta")
    condiciones = peticion.json()

    for i, val in enumerate(condiciones):
        condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
                "stock": val.get("cantidad_en_stock"),
                "base": val.get("precio_proveedor")
            }
    return condiciones

def menu():
    while True:
        os.system("clear")
        print("""  
    ____                        __                   __                             __           __            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                             /_/                                                  

            1. Obtener todos los productos de una categoría ordenando sus precios de venta, también que su cantidad de inventario sea superior (ejem: Ornamentales, 100 )
            0. Atras
          
          """)        
        opcion = input("\nSelecione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion>=0 and opcion<=1):
                if(opcion == 1):
                    gama = input("Ingrese la gama que deseas flictrar: ")
                    stock = int(input("Ingrese las unidades que seas mostrar: "))
                    print(tabulate(getAllStocksPriceGama(gama, stock), headers="keys", tablefmt="github"))
                    input("Precione una tecla para continuar.....")
                elif(opcion == 0):
                    break
