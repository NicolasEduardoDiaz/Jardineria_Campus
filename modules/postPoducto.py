import json


#servidor
#http://172.16.100.128:5401


def postProduct(producto):
    import requests
    peticion = requests.post("http://172.16.100.128:5401", data =json.dump(producto))
    res = peticion.json()
    return res