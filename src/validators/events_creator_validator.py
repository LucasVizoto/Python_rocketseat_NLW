# vamos criar as validações para dizer se o body
# da requisição está correto

from cerberus import Validator

def events_creator_validator(request: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": { "type": "string", "required": True, "empty": False }
            }
        }
    })

    response = body_validator.validate(request.json)

    if response is False: #Fazendo uma barreira
        raise Exception(body_validator.errors)