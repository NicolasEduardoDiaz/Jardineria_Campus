import storage.pedido as ped

def getEstadoPedido():
    estadosPedido = set()
    for val in ped.pedido:
        estado_pedido = val.get('estado')
        estadosPedido.add(estado_pedido)
    return estadosPedido
