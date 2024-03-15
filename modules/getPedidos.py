import storage.pedido as ped
from tabulate import tabulate

def getEstadoPedido():
    estadosPedido = list()
    for val in ped.pedido:
        estado_pedido = val.get('estado')
        estadosPedido.add(estado_pedido)
    return estadosPedido
