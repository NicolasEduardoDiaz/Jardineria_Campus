from tabulate import tabulate

import modulos.getClients as cliente

print(tabulate(cliente.getAllClientPaisRegionCiudad("Spain", "fuenlabrada", "Madrid"), tablefmt = 'grid'))
from tabulate import tabulate 
import modulos.getEmpleados as empleado
import modulos.getClients as clientes
import modulos.getOficina as oficina
import modulos.getPedidos as pedido
import modulos.getPago as pago

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