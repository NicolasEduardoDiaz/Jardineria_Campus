import requests
import json
from datetime import datetime

def getAll():
    peticion = requests.get("http://154.38.171.54:5007/pedidos")
    data = peticion.json()
    return data


# Devuelve un listado con el código de pedido, 
# código de cliente, fecha esperada y 
# fecha de entrega de los pedidos que no 
# han sido entregados a tiempo.
def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado")
    data = peticion.json()

    for val in data:
        if val.get("fechaEntrega") is None:
            val["fechaEntrega"] = val.get("fecha_esperada")

        date_1 = "/".join(val.get("fechaEntrega").split("-")[::-1]) 
        date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
        start = datetime.strptime(date_1, "%d/%m/%Y")
        end =   datetime.strptime(date_2, "%d/%m/%Y")
        diff = end.date() - start.date()
        if(diff.days < 0):
            pedidosEntregado.append({
                "código_de_pedido": val.get("codigo_pedido"),
                "código_de_cliente": val.get("codigo_cliente"),
                "fecha_esperada": val.get("fecha_esperada"),
                "fecha_de_entrega": val.get("fechaEntrega"),
                "dias_de_retraso": -(diff.days)
            })
            
    return pedidosEntregado

# Devuelve un listado de todos los pedidos que han sido entregados 
# en el mes de enero de cualquier año.