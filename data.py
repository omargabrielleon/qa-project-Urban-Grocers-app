#Config para el POST

'''Datos de la solicitud: crea un archivo llamado data.py.
Este archivo almacenará la información que se enviará en la solicitud,
como el cuerpo y los encabezados:
'''

headers = {
    "Content-Type": "application/json"
    }

user_body = {
    "firstName": "Andrea",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

kit_body = {
       "name": "Mi conjunto"
}

kit_body_1 = {
       "name": "a"
}

kit_body_2 = {
    "name": "a" * 511
}

kit_body_3 = {
       "name": ""
}

kit_body_4 = {
    "name": "a" * 512
}

kit_body_5 = {
        "name": "\№%@\,"
}

kit_body_6 =  {
        "name": "A Aaa"
}

kit_body_7 =  {
        "name": "123"
}

Kit_body_8 =  {

}

Kit_body_9 =  {
        "name": 123
}


