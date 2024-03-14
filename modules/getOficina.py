import storage.oficina as of
from tabulate import tabulate

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if val.get("pais") == pais:
            ciudadTelefono.append({
                "ciudad": val.get("ciudad"),
                "telefono": val.get("telefono"),
                "oficinas": val.get("codigo_oficina"),
                "pais": val.get("pais") 
            })
    return ciudadTelefono

def getAllDirecciones():
    Direcciones = []
    for val in of.oficina:
        Direcciones.append({
            "Codigo Oficina": val.get("codigo_oficina"),
            "Pais": val.get("pais"),
            "Ciudad": val.get("ciudad"),
            "Direccion": f'{val.get("linea_direccion1")}, {val.get("linea_direccion2")}'
        })
    return Direcciones

def menu():
    while True:
        print("""
                          ____                        __                   __        ____  _____      _                 
                         / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / __ \/ __(_)____(_)___  ____ ______
                        / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / / / /_/ / ___/ / __ \/ __ `/ ___/
                       / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
                      /_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  
                                /_/                                                                                     
                                            1. Obtener el código de la oficina y su ciudad.
                                            2. Obtener información según el país.
                                            3. Obtener las direcciones de las oficinas.
                                            0. Regresar al menú principal.
""")
    
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="rounded_grid"))
        elif opcion == "2":
            pais = input("Ingrese el país: ")
            print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="rounded_grid"))
        elif opcion == "3":
            print(tabulate(getAllDirecciones(), headers="keys", tablefmt="rounded_grid"))
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()

