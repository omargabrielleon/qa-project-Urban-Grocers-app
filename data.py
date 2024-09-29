#Config para el POST

'''Datos de la solicitud: crea un archivo llamado data.py.
Este archivo almacenará la información que se enviará en la solicitud,
como el cuerpo y los encabezados:
'''

headers = {
    "Content-Type": "application/json"
}


user_body = {
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}


kit_body_a = {
    "name": "a"
}

kit_body_511 = {
    "name": "El valor de prueba para esta comprobación será inferior a" + "a" * 463  # Total 511 caracteres
}

