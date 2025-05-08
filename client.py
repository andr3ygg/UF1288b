import requests
import json
from server import LOCAl_IP
from server import DEFAULT_PORT


URL = f"http://{LOCAl_IP}:{DEFAULT_PORT}/"


def main():
    response = requests.get(URL)
    return(response)



def mensaje():
    headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
    }

    mensaje = input("Mensaje: ")
    json_datos = {
        'mensaje': 'HOLA MUNDO',
    }

    enviar = requests.post(URL, json=json_datos, headers=headers)
    print(enviar)

mensaje()