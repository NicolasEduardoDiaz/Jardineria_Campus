from datetime import datetime
from tabulate import tabulate

import storage.pago as pag

def getPagosByYearAndMethod(year, method):
    pagos = []
    for val in pag.pago:
        fecha_pago = "/".join(val.get("fecha_pago").split("-")[::-1])
        start = datetime.strptime(fecha_pago, "%d/%m/%Y")
        if start.year == year and val.get("forma_pago") == method:
            pagos.append(val)
    return pagos

def getAllFormasDePago():
    formas_pago = set(val.get("forma_pago") for val in pag.pago)
    return [{"Formas De Pago:": forma} for forma in formas_pago]

def menu():
    while True:
        print("""

                        ____                        __              __        
                       / __ \___  ____  ____  _____/ /____     ____/ /__      
                      / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \   / __  / _ \     
                     / _, _/  __/ /_/ / /_/ / /  / /_/  __/  / /_/ /  __/     
                    /_/ |_|\___/ .___/\____/_/   \__/\___/   \__,_/\___/      
                         ____  /_/_ _____ _____  _____                         
                        / __ \/ __ `/ __ `/ __ \/ ___/                         
                       / /_/ / /_/ / /_/ / /_/ (__  )                          
                      / .___/\__,_/\__, /\____/____/                           
                     /_/          /____/                                       

1. Obtener lista de pagos realizados en 2008.
2. Obtener lista de pagos realizados por medio de "Paypal".
3. Obtener lista de formas de pago.  

0. Regresar al menú principal.        
          """)
    
        opcion = int(input("Seleccione una de las opciones: "))
        
        if opcion == 1:
            year = 2008
            method = None
            print(tabulate(getPagosByYearAndMethod(year, method), headers="keys", tablefmt="rounded_grid"))

        if opcion == 2:
            year = 2008
            method = "Paypal"
            print(tabulate(getPagosByYearAndMethod(year, method), headers="keys", tablefmt="rounded_grid"))

        if opcion == 3:
            print(tabulate(getAllFormasDePago(), headers="keys", tablefmt="rounded_grid"))
            
        if opcion == 0:
            break

menu()

