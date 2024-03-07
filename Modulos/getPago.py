import storage.pago as pag


def getFechaPago():
    FechaPago = set()
    for val in pag.pago:
        if val.get('fecha_pago').startswith("2008"):
            FechaPago.add(val.get("codigo_cliente"))
    return FechaPago