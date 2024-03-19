from tabulate import tabulate
import json
import requests
import os
import re
import modules.getGama as gG
import modules.getProductos as gP

def postProducto():
    # json-server storage/producto.json -b 5501
    producto = dict()
    # while True:
    #     try:
    #         # expresion regular que valide de una cadena Numeros y letras en myusculas pero la cadena es de 6 caracteres los primeros 2 son las letras en mayusculas segido de un - y los 3 ultimos caracteres son numeros:
    #         if(not producto.get("codigo_producto")):
    #             codigo = input("Ingrese el codigo del producto: ")
    #             if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
    #                 data = gP.getProductCodigo(codigo)
    #                 if(data):
    #                     print(tabulate(data, headers="keys", tablefmt="github"))
    #                     raise Exception("El codigo producto ya existe")
    #                 else:
    #                     producto["codigo_producto"] = codigo
    #             else:
    #                 raise Exception("El codigo producto no cumple con el estandar establecido")

    #         # expresion regular que valida de una cadena solo letras pero que las primeras letras de cada palabra sea en mayusculas y las demas en minusculas respetando los espacios por cada palabra y que tambien se pueda ingresar una sola palabra
    #         if(not producto.get("nombre")):
    #             nombre = input("Ingrese el nombre del producto: ")
    #             if(re.match(r'^([A-Z][a-z]*\s*)+$', nombre) is not None):
    #                 producto["nombre"] = nombre
    #                 break
    #             else:
    #                 raise Exception("El nombre del producto no cumple con el estandar establecido")

    #     except Exception as error:
    #         print(error)
    # print(producto)

    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": input("Ingrse la dimensiones del producto: "),
        "proveedor": input("Ingrse el proveedor del producto: "),
        "descripcion": input("Ingrse el descripcion del producto: "),
        "cantidadEnStock": int(input("Ingrse el cantidad en stock: ")),
        "precio_venta": int(input("Ingrse el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrse el precio del proveedor: "))
    }

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5008/productos", headers=headers, data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def deleteProducto(id):
    data = gP.getProductCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.102.108:5501/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "producto eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"producto no encontrado",
                "id": id
            }],
            "status": 400,
        }

def menu():
    while True:
        os.system("clear")
        print("""  
    ___       __          _       _      __                         __      __                    __        
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__      
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \     
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/     
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/      
    ____  ____  ____  ____  __  __________________  _____                                                   
   / __ \/ __ \/ __ \/ __ \/ / / / ____/_  __/ __ \/ ___/                                                   
  / /_/ / /_/ / / / / / / / / / / /     / / / / / /\__ \                                                    
 / ____/ _, _/ /_/ / /_/ / /_/ / /___  / / / /_/ /___/ /                                                    
/_/   /_/ |_|\____/_____/\____/\____/ /_/  \____//____/                                                     
                                                                                                                                                    
            1. Guardar un producto nuevo
            2. Eliminar un producto
            0. Atras
          
          """)        
        opcion = input("\nSelecione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if(opcion>=0 and opcion<=2):
                if(opcion == 1):
                    print(tabulate(postProducto(), headers="keys", tablefmt="github"))
                elif(opcion == 2):
                    idProducto = input("Ingrese el id del producto que desea eliminar: ")
                    # deleteProducto(idProducto)
                    print(tabulate(deleteProducto(idProducto)["body"], headers="keys", tablefmt="github"))
                elif(opcion == 0):
                    break

        input("Precione una tecla para continuar.....")