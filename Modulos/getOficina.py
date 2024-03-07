import storage.oficina as ofi

def getCodigoOfiCiudadName():
    CodigoOfiCiudad = list()
    for val in ofi.oficina:
        codigoNames = dict({
            "codigo_oficina": val.get('codigo_oficina'),
            "ciudad": val.get('ciudad')
        })
        CodigoOfiCiudad.append(codigoNames)
    return CodigoOfiCiudad

def getCiudadTelefonoEspaña():
    ciudadTelefonoEspaña = []
    for val in ofi.oficina:
        if val.get('pais') == "España" :
            ciudadTelefonoEspaña.append(
                {
                    "ciudad": val.get("ciudad"),
                    "telefono": val.get("telefono")
                }
            )  
    return ciudadTelefonoEspaña
