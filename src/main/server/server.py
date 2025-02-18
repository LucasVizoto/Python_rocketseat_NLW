from flask import Flask

from src.main.routes.event import event_route_bp

app = Flask(__name__)
# criando um servidor http

app.register_blueprint(event_route_bp)
#registrei meu agregador no servidor