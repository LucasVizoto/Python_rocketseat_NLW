#este arquivo é onde eu cadastro as minhas rotas para acessá-las posteriormente

from flask import Flask

from src.main.routes.event import event_route_bp
from src.main.routes.subs import subs_route_bp
app = Flask(__name__)
# criando um servidor http


app.register_blueprint(event_route_bp)
app.register_blueprint(subs_route_bp)
#registrei meu agregador no servidor