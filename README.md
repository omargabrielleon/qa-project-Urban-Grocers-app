## Proyecto para el séptimo sprint: Tarea

######  Otro QA Engineer que trabaja contigo está comprobando cómo la aplicación Urban Grocers crea kits de productos. Se han creado varias listas de comprobación, una de ellas es para el campo name en la solicitud de creación de un kit de productos. Tu tarea es automatizar las pruebas desde esta lista de comprobación, cargar el código en GitHub y enviar el repositorio a revisión.
#
#
#### Creación de un kit para el usuario o usuaria
Vas a crear un kit dentro de un usuario o usuaria particular, no una tarjeta. Para ello, sigue estos pasos:

1). Envía una solicitud para crear un nuevo usuario o usuaria y recuerda el token de autenticación (authToken).
 
 2). Envía una solicitud para crear un kit personal para este usuario o usuaria. Asegúrate de pasar también el encabezado Autorization.
Después de eso, simplemente utiliza la lista de comprobación. Los resultados de la prueba serán diferentes cada vez, según el cuerpo de solicitud. Sin embargo, los pasos serán los mismos.

3). Trabajamos con un servidor para la URL del proyecto y uno para la documentacion de pruebas.
Dirección del banco: https://cnt-3fc2b06d-74e2-46f1-ab02-82cd2ef72523.containerhub.tripleten-services.com
Documentación de la API: https://cnt-3fc2b06d-74e2-46f1-ab02-82cd2ef72523.containerhub.tripleten-services.com/docs/

# Listas de comprobacion
| 	Description  | 	ER: |
| No. of test | 	Description  | 	ER:  |
| :---         |     :---:      |          ---: |
| 1   | El número permitido de caracteres (1): kit_body = { "name": "a"}     | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud    |
| 2   | El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}     | Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud    |
| 3   | El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }     | Código de respuesta: 400    |
| 4   | El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }     | Código de respuesta: 400   |
| 5   | Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }     | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud    |
| 6   | Se permiten espacios: kit_body = { "name": " A Aaa " }     | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud    |
| 7   | Se permiten números: kit_body = { "name": "123" }     | Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud    |
| 8   | El parámetro no se pasa en la solicitud: kit_body = { }     | Código de respuesta: 400    |
| 9   | Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }     | Código de respuesta: 400    |


## Features

- El proyecto cuenta con 6 archivos: gitignore, configuration.py, create_kit_name_kit_test.py, data.py, README.md y sender_stand_request.py

- Se instalaron los siguientes packages en Pycharm: pytest, requests

- configuration.py contiene:
    >URL_SERVICE = "https://cnt-264508f5-223b-4d3c-baf3-a2acf1fe9431.containerhub.tripleten-services.com" # Inserta tu dirección de URL sin la barra diagonal al final
    >CREATE_USER_PATH = "/api/v1/users" # Almacena la ruta para crear un usuario o usuaria en esta variable
    >KITS_PATH = "/api/v1/kits" # Almacena la ruta para crear un kit en esta variable
- data.py contiene:
    >#Config para el POST

    >'''Datos de la solicitud: crea un archivo llamado data.py.
Este archivo almacenará la información que se enviará en la solicitud,
como el cuerpo y los encabezados

- sender_stand_request.py contiene:
    >'''
#Creacion de nuevo usuario con sus elementos de REQUEST
#Metodo: post
#URL: que viene de el archivo configuration.py (configuration.URL_SERVICE +
#End_point: que viene tambien del archivo configuration.py configuration.CREATE_USER_PATH,
#Parametros: json y headers
'''

        import requests
        import configuration
        import data
        

    >[!NOTE] 
    def post_new_kit(auth_token, kit_info): # Funcion para la creacion del kit
    headers_with_Authorization = data.headers.copy() #copiamos de data los headers
    headers_with_Authorization ["Authorization"] = f"Bearer {auth_token}" #
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
             json=kit_info,
                 headers=headers_with_Authorization,) # Llamamos al servidor con la URL, y el call kit_path para la creacion del kit, usando json la informacion del kit y en el header la autorizacion.'''
- create_kit_name_kit_test.py contiene:

        import sender_stand_request
        import data
        from sender_stand_request import post_new_kit, response

    >[!NOTE]
def positive_assert(kit_body):
    response_kit_body = post_new_kit(sender_stand_request.get_atk_from_body(), kit_body)
    assert response_kit_body.status_code == 201
    assert response_kit_body.json()["name"] == kit_body ["name"]

    >[!NOTE]
def negative_assert_code_400(kit_body):
    response_kit_body = post_new_kit(sender_stand_request.get_atk_from_body(), kit_body)
    assert response_kit_body.status_code == 400

    >[!NOTE]
def test_create_kit_body_1_letter_in_first_name_get_success_response():
    positive_assert(data.kit_body_1)

## Tech

- [Pycharm] - IDE, desarrollo, Python.
- [Terminal] - Interfaz, comandos, shell.
- [Git] - Control, versiones, código.
- [GitHub] - Repositorio, colaboración, Git.