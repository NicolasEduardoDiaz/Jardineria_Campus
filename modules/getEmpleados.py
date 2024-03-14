import storage.empleado as em
from tabulate import tabulate

def getAllNombreApellidoEmailJefe(codigo):
    NombreApellidoEmail = []
    for val in em.empleado:
        if val.get("codigo_jefe") == codigo:
            NombreApellidoEmail.append({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email"),
                "jefe": val.get("codigo_jefe")
            })
    return NombreApellidoEmail

def getAllPuestoNombreApellidosEmailJefe():
    DatosJefe = []
    for val in em.empleado:
        if val.get("codigo_jefe") is None:
            DatosJefe.append({
                "Puesto": val.get("puesto"),
                "Nombre": val.get("nombre"),
                "Apellido": val.get("apellido1"),
                "Email": val.get("email")
            })
    return DatosJefe

def getAllNombreApellidosPuestoNoRepVentas():
    InfoNoRepVentas = []
    for val in em.empleado:
        if val.get("puesto") != "Representante Ventas":
            InfoNoRepVentas.append({
                "Puesto": val.get("puesto"),
                "Nombre": val.get("nombre"),
                "Apellido": val.get("apellido1"),
            })
    return InfoNoRepVentas

def menu():
    while True:
        print("""
              ____                        __              __                             __               __          
             / __ \___  ____  ____  _____/ /____     ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____
            / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
           / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
          /_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                    /_/                                                       /_/                                     

        1. Obtener información con el código del jefe.
        2. Obtener información del director general.
        3. Obtener nombres de empleados que no son representantes de ventas.
        0. Regresar al menú principal.
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                codigojefe = int(input("Ingrese el código de jefe: "))
                print(tabulate(getAllNombreApellidoEmailJefe(codigojefe), headers="keys", tablefmt="rounded_grid"))
            except ValueError:
                print("Error: Debe ingresar un número válido.")
        elif opcion == "2":
            print(tabulate(getAllPuestoNombreApellidosEmailJefe(), headers="keys", tablefmt="rounded_grid"))
        elif opcion == "3":
            print(tabulate(getAllNombreApellidosPuestoNoRepVentas(), headers="keys", tablefmt="rounded_grid"))
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()

