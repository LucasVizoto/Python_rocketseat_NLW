# vou separar o que eu vou querer da minha requisição
class HttpRequest:

    def __int__(self, body: dict, param: dict = None) -> None:
        self.body = body
        self.status_code = param