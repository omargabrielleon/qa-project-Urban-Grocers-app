'''
#Creacion de nuevo usuario con sus elementos de REQUEST
#Metodo: post
#URL: que viene de el archivo configuration.py (configuration.URL_SERVICE +
#End_point: que viene tambien del archivo configuration.py configuration.CREATE_USER_PATH,
#Parametros: json y headers
'''

import configuration
import requests
import data



def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body) #Variable que almacena la funcion (data.user_body)
print(response.status_code)
print(response.json())



def get_atk_from_body():
    answer_server = post_new_user(data.user_body)
    # Respuesta del servidor con la data de user_body que se uso en la funcion anterior
    authToken = answer_server.json()["authToken"]
    # De la respuesta del servidor tomar el authoken
    return authToken #solo se guarda el retorno del authoken sin imprimir para
#posteriormente llamar a la funcion en la creacion del kit.



def post_new_kit(auth_token, kit_info): # Funcion para la creacion del kit
    headers_with_Authorization = { # Llave con mi header y mi auhtoken
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                json=kit_info,
                  headers=headers_with_Authorization,) # Llamamos al servidor con la URL, y el call kit_path
#para la creacion del kit, usando json la informacion del kit y en el header la autorizacion.
