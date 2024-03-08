from tabulate import tabulate

import modules.getClients as cliente


from tabulate import tabulate 
import modules.getEmpleados as empleado
import modules.getClients as clientes
import modules.getOficina as oficina
import modules.getPedidos as pedido
import modules.getPago as pago
import sys

if(__name__=="_name_"):
    print(f"""
      __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/          
                         1.cliente
                         2.oficina
                         3.empleado
                         4.pedidos
   """)
    opcion = int(input("\nseleccione una de las opciones"))
    if(opcion==1):
        cliente.menu()
    elif():

#print(tabulate(cliente.getAllClientPaisRegionCiudad("Spain", "fuenlabrada", "Madrid"), tablefmt = 'grid'))
   #Todos los nombres de los empleados
#print(tabulate(empleado.getAllEmpleadosName()), tablefmt="grid")

   #Filtrar la informacion por el codigo de jefe correspondiente
#print(tabulate(empleado.getAllEmpleadosCode(15)))

   #La informacion del nombre de la persona 
#print(tabulate(empleado.getOneEmpleadoNombreApellidos("Ruben")tablefmt = 'grid'))

   #Con el codigo del empleado y opcional el nombre muestra la informacion
#print(tabulate(empleado.getOneEmpleadoCodeNombre(17)tablefmt = 'grid'))

   #Filtrar la informacion por el codigo de jefe correspondiente
#print(tabulate(empleado.getAllEmpleadosCode(15)))

    #
#print(tabulate(empleado.getOneEmpleadoExtension("Representante Ventas")))

#PUNTOS PAGINA

   #1 punto
#print(tabulate(oficina.getCodigoOfiCiudadName()))

   #2 punto
#print(tabulate(oficina.getCiudadTelefonoEspaña()))

   #3 punto
#print(tabulate(empleado.getNombreApellidoEmailJefe()))

   #4 punto
#print(tabulate(empleado.getAllJefesCode()))

   #5 punto
#print(tabulate(empleado.getEmpleadosPuesto()))

   #6 punto
#print(tabulate(clientes.getNombreClientesEspaña()))

   #7 punto
#print(tabulate(pedido.getEstadoPedido()))

   #8 punto
#print(tabulate(pago.getFechaPago()))

   #EJERCICIOS PRACTICA

   #Todos los nombres de los empleados
#print(tabulate(empleado.getAllEmpleadosName()), tablefmt="grid")

   #Filtrar la informacion por el codigo de jefe correspondiente
#print(tabulate(empleado.getAllEmpleadosCode(15)))

   #La informacion del nombre de la persona 
#print(tabulate(empleado.getOneEmpleadoNombreApellidos("Ruben")))

   #Con el codigo del empleado y opcional el nombre muestra la informacion
#print(tabulate(empleado.getOneEmpleadoCodeNombre(17)))

   #Filtrar la informacion por el codigo de jefe correspondiente
#print(tabulate(empleado.getAllEmpleadosCode(15)))

   #Muestra toda la información de las personas que no son representante de ventas
#print(tabulate(empleado.getOneEmpleadoExtension("Representante Ventas")))