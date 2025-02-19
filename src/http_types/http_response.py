# criando um padrão de resposta http

class HttpResponse:
    def __init__(self, body: dict, status_code: int) -> None:
        self.body = body
        self.status_code = status_code

