import Storage.cliente as cli

def getAllClientesName():
    clienteName = []
    for i,val in cli.clientes:
        codigoNames= dict({
            "codigo_cliente": val.get("codigo_cliente"),
            "nombre_cliente": val.get("nombre_cliente")
        })
        clienteName.append(codigoNames)
    return clienteName

def getOneClienteCodigo(codigo):
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
            return{
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            }
        
def getAllClientCreditCiudad(limiteCredit, Ciudad):
    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_cliente') >= limiteCredit and val.get ('ciudad') == Ciudad):
            clienteCredic.append(val)
    return clienteCredic

def getAllClientPaisRegionCiudad(pais, region=None,ciudad=None):
    clientZone = list()
    for val in cli.clientes:
        if(
            val.get('pais') == pais and 
            (val.get('region') == region or val.get('region') == None) or
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
            clientZone.append(val)
    return clientZone