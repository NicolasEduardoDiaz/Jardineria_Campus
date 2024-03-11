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