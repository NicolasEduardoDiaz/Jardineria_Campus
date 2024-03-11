import storage.cliente as cli
from tabulate import tabulate

def search():
    ClienteName = list()
    for val in cli.clientes:
        codName = dict({
            "Codigo": val.get("codigo_cliente"),
            "Nombre": val.ger("nombre_cliente")
        })
        ClienteName.append(codName)
    return ClienteName

def getOneClienteCodigo(codigo):
    for val in cli.clientes:
        if(val.get("codigo_cliente") == codigo):
            return[{
                "codigo_cliente": val.get("codigo_cliente"),
                "nombre_cliente": val.get("nombre_cliente")
            }]
            
def getAllClientsCreditCiudad(limiteCredit, ciudad):
    clienteCredito = list()
    for val in cli.clientes:
        if(val.get("limite_credito") >= limiteCredit and val.get("ciudad") == ciudad):
            clienteCredito.append({
                "codigo": val.get("codigo_cliente"),
                "Nombre": val.get("nombre_cliente"),
                "Contacto":f'{val.get("nombre_comtacto")} {val.get("apellido_contacto")}',
                "Telefono":val.get ("telefono"),
                "Fax": val.get("fax"),
                "Direccion": f'{val.get("linea_direccion")} / {val.get("linea_direccion2")}',
                "Pais": val.get("pais"),
                "Ciudad": val.get("ciudad"),
                "Codigo postal": val.get("codigo_postal"),
                "Codigo rep. de venta": val.get("codigo_empleado_rep_ventas"),
                "limite de credito": val.get("limite_credito")
            })
        return clienteCredito
    
def  getAllClientsPaisRegionCiudad(Pais, Region=None, Ciudad = None):
    ClienteZona = list()
    for val in cli.clientes:
        if (
            val.get("pais") == Pais or 
            (val.get("region") == Region or val.get("region")== None) and
            (val.get("ciudad") == Ciudad or val.get("ciudad") == None)
        ):
            ClienteZona.append(val)
    return ClienteZona

def getAllClientsMismoFax(Fax):
    ClienteFax = list()
    for val in cli.clientes:
        if (val.get("fax") == Fax):
            ClienteFax.append({
                "Codigo":val.get("codigo_cliente"),
                "Nombre":val.get("nombre_cliente"),
                "Contacto":f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Telefono":val.get("telefono"),
                "Fax":val.get("fax"),
                "Direccion": f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}',
                "Pais":val.get("pais"),
                "Ciudad":val.get("ciudad"),
                "Codigo Postal":val.get("codigo_postal"),
                "Codigo rep. de ventas":val.get("codigo_empleado_rep_ventas"),
                "Limite de Credito":val.get("limite_credito")
            })
        return ClienteFax
    
def getAllClientsMismoCodigo_empleado_rep_ventas(Codigo):
    CodigoEmpleado = list()
    for val in cli.clientes:
        if val.get("codigo_empleado_rep_ventas") == Codigo:
            CodigoEmpleado .append({
                "Codigo":val.get("codigo_cliente"),
                "Nombre":val.get("nombre_cliente"),
                "Contacto":f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Telefono":val.get("telefono"),
                "Fax":val.get("fax"),
                "Direccion": f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}',
                "Pais":val.get("pais"),
                "Ciudad":val.get("ciudad"),
                "Codigo Postal":val.get("codigo_postal"),
                "Codigo rep. de ventas":val.get("codigo_empleado_rep_ventas"),
                "Limite de Credito":val.get("limite_credito")

            })
        return CodigoEmpleado
    
def getAllClientsNombrePostal():
    NombreYPostal = list()
    for val in cli.clientes:
        datos = dict({"Nombre Clientes": val.get("nombre_cliente"), "Codigo Postal": val.get("codigo_postal")})
        NombreYPostal.append(datos)
    return NombreYPostal

def getAllClientsDirecciones():
    direcciones= list()
    for val in cli.clientes:
        direccion1y2 = dict({"Nombre":val.get("nombre_cliente"), "Direccion":f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}'})
        direcciones.append(direccion1y2)
    return direcciones

def getAllClientsApellidoContacto(apellido):
    apellidos = list()
    for val in cli.clientes:
        if(val.get("apellido_contacto") == apellido):
            apellidos.append({
                  "Codigo":val.get("codigo_cliente"),
                "Nombre":val.get("nombre_cliente"),
                "Contacto":f'{val.get("nombre_contacto")} {val.get("apellido_contacto")}',
                "Telefono":val.get("telefono"),
                "Fax":val.get("fax"),
                "Direccion": f'{val.get("linea_direccion1")} / {val.get("linea_direccion2")}',
                "Pais":val.get("pais"),
                "Ciudad":val.get("ciudad"),
                "Codigo Postal":val.get("codigo_postal"),
                "Codigo rep. de ventas":val.get("codigo_empleado_rep_ventas"),
                "Limite de Credito":val.get("limite_credito")
            })
    return apellidos


def getAllNombreSpain():
    nombreEspaña = list()
    for val in cli.clientes:
        if val.get("pais") == "Spain":
            nombreEspaña.append({"nombre":val.get("nombre_cliente"),
                                 "Pais":val.get("Pais")})
        return nombreEspaña

def menu(): 
    while True: 
        print(f"""
  _______                                           __                           __                   ______   __  __                      __                       
 |       \                                         |  \                         |  \                 /      \ |  \|  \                    |  \                      
 | $$$$$$$\  ______    ______    ______    ______ _| $$_    ______          ____| $$  ______        |  $$$$$$\| $$ \$$  ______   _______ _| $$_    ______   _______ 
 | $$__| $$ /      \  /      \  /      \  /      \   $$ \  /      \        /      $$ /      \       | $$   \$$| $$|  \ /      \ |       \   $$ \  /      \ /       \
 | $$    $$|  $$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\$$$$$$ |  $$$$$$\      |  $$$$$$$|  $$$$$$\      | $$      | $$| $$|  $$$$$$\| $$$$$$$\$$$$$$ |  $$$$$$\  $$$$$$$
 | $$$$$$$\| $$    $$| $$  | $$| $$  | $$| $$   \$$| $$ __| $$    $$      | $$  | $$| $$    $$      | $$   __ | $$| $$| $$    $$| $$  | $$| $$ __| $$    $$\$$    \ 
 | $$  | $$| $$$$$$$$| $$__/ $$| $$__/ $$| $$      | $$|  \ $$$$$$$$      | $$__| $$| $$$$$$$$      | $$__/  \| $$| $$| $$$$$$$$| $$  | $$| $$|  \ $$$$$$$$_\$$$$$$\
 | $$  | $$ \$$     \| $$    $$ \$$    $$| $$       \$$  $$\$$     \       \$$    $$ \$$     \       \$$    $$| $$| $$ \$$     \| $$  | $$ \$$  $$\$$     \       $$
  \$$   \$$  \$$$$$$$| $$$$$$$   \$$$$$$  \$$        \$$$$  \$$$$$$$        \$$$$$$$  \$$$$$$$        \$$$$$$  \$$ \$$  \$$$$$$$ \$$   \$$  \$$$$  \$$$$$$$\$$$$$$$ 
                     | $$                                                                                                                                           
                     | $$                                                                                                                                           
                      \$$                                                                                                                                           
                      
                      1. Obtener el Nombre y el codigo de los clientes.
                      2. Obtener Un cliente por codiogo.
                      3. Obtener la informacion por el limite de credito y la ciudad.
                      4. Obtener la informacion de los clientes segun el fax. 
                      5. Obtener la informacion por el codigo de representante de venta. 
                      6. Obtener el nombre y la postal del cliente. 
                      7. Obtener la direccion de los clientes
                      8. Obtener la informacion de los clientes por su apellido. 
                      9. Obtener los nombres de los clientes que viven en España.
                      
                      0. Salir al menú
                """)