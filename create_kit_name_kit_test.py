import sender_stand_request  # Asegúrate de que el import sea correcto
import data  # Importamos el kit_body y los headers desde data.py

# Prueba para crear un kit con 1 carácter en el campo "name"
def test_create_kit_with_one_char_name():
    # Crear kit con nombre de un solo carácter y verificar la respuesta
    kit_response = sender_stand_request.post_new_kit(
        sender_stand_request.get_atk_from_body(),
        data.kit_body_a
    )

    assert kit_response.status_code == 201, f"Expected 201, got {kit_response.status_code}"
    assert kit_response.json()["name"] == data.kit_body_a["name"], \
        f"Expected name '{data.kit_body_a['name']}', got '{kit_response.json()['name']}'"

    print(f"Status Code: {kit_response.status_code}, Response: {kit_response.json()}")


def test_create_kit_with_511_char_name():
    # Crear kit con nombre de 511 caracteres y verificar la respuesta
    kit_response = sender_stand_request.post_new_kit(
        sender_stand_request.get_atk_from_body(),
        data.kit_body_511
    )

    assert kit_response.status_code == 201, f"Expected 201, got {kit_response.status_code}"
    assert kit_response.json()["name"] == data.kit_body_511["name"], \
        f"Expected name '{data.kit_body_511['name']}', got '{kit_response.json()['name']}'"


def test_create_kit_with_empty_name():
    # Crear kit con nombre vacío y verificar que se recibe un error
    kit_response = sender_stand_request.post_new_kit(
        sender_stand_request.get_atk_from_body(),
        {"name": ""}
    )

    assert kit_response.status_code == 400, f"Expected 400, got {kit_response.status_code}"
    expected_error_message = "Name cannot be empty"
    assert expected_error_message in kit_response.json().get("error", ""), \
        f"Expected error message '{expected_error_message}', got '{kit_response.json().get('error', '')}'"


def test_create_kit_with_name_greater_than_512_characters():
    # Crear kit con un nombre que excede 512 caracteres
    kit_body = {"name": "A" * 513}
    kit_response = sender_stand_request.post_new_kit(
        sender_stand_request.get_atk_from_body(),
        kit_body
    )
    # Verificar que el código de estado es 400
    assert kit_response.status_code == 400, f"Expected 400, got {kit_response.status_code}"

def test_create_kit_with_special_characters_in_name():
    # Crear kit con caracteres especiales
    kit_body = {"name": "№%@,"}
    kit_response = sender_stand_request.post_new_kit(
        sender_stand_request.get_atk_from_body(),
        kit_body
    )
    # Verificar estado y coincidencia de nombre
    assert kit_response.status_code == 201, f"Expected 201, got {kit_response.status_code}"
    assert kit_response.json()["name"] == kit_body["name"], \
        f"Expected name '{kit_body['name']}', got '{kit_response.json()['name']}'"


def test_create_kit_with_spaces_in_name():
    # Obtener token y crear kit con nombre que contiene espacios
    kit_body_with_spaces = {"name": " A Aaa "}
    kit_response = sender_stand_request.post_new_kit(sender_stand_request.get_atk_from_body(), kit_body_with_spaces)

    # Verificar que el código de estado es 201 y el nombre en la respuesta coincide
    assert kit_response.status_code == 201, f"Expected status code 201, got {kit_response.status_code}"
    assert kit_response.json()["name"] == kit_body_with_spaces["name"], \
        f"Expected name '{kit_body_with_spaces['name']}', got '{kit_response.json()['name']}'"


def test_create_kit_with_numbers_in_name():
    # Crear kit con nombre que contiene números y verificar la respuesta
    kit_body_with_numbers = {"name": "123"}  # Cuerpo de la solicitud con números

    kit_response = sender_stand_request.post_new_kit(
        sender_stand_request.get_atk_from_body(),
        kit_body_with_numbers
    )

    assert kit_response.status_code == 201, f"Expected 201, got {kit_response.status_code}"
    assert kit_response.json()["name"] == kit_body_with_numbers["name"], \
        f"Expected name '{kit_body_with_numbers['name']}', got '{kit_response.json()['name']}'"


def test_create_kit_with_numeric_name_parameter():
    # Enviar solicitud con un número como nombre y verificar respuesta
    kit_response = sender_stand_request.post_new_kit(
        sender_stand_request.get_atk_from_body(),
        {"name": 123}  # 'name' es un número
    )

    # Verificar que el código de estado sea 400 y el mensaje de error esperado
    assert kit_response.status_code == 400, f"Expected 400, got {kit_response.status_code}"
    assert "Invalid type for name" in kit_response.json().get("error", ""), \
        f"Unexpected error message: {kit_response.json().get('error', '')}"

def test_create_kit_with_numeric_name_parameter():
    # Cuerpo de la solicitud con un número como nombre
    kit_response = sender_stand_request.post_new_kit(
        sender_stand_request.get_atk_from_body(),
        {"name": 123}  # 'name' es un número
    )
    # Verificar que el código de estado sea 400
    assert kit_response.status_code == 400, f"Expected 400, got {kit_response.status_code}"
    # Verificar el mensaje de error en la respuesta (ajustar según la implementación)
    assert "Invalid type for name" in kit_response.json().get("error", ""), \
        f"Unexpected error message: {kit_response.json().get('error', '')}"

