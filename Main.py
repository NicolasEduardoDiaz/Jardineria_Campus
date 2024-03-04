from tabulate import tabulate

import Modulos.getClients as cliente

print(tabulate(cliente.getAllClientPaisRegionCiudad("Spain", "fuenlabrada", "Madrid"), tablefmt = 'grid'))
