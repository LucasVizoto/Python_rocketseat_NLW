from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos import Eventos

class EventosRepository:
    def insert(self, event_name: str) -> None:
        with DBConnectionHandler() as db:
            try:
                new_event = Eventos(nome = event_name)
                db.session.add(new_event) #adicionei para a minha sessão um novo evento
                db.session.commit()

            except Exception as exception:
                db.session.rollback() # se deu certo eu dou um commit, se cair na excessão, rollback e raise da exceção
                raise exception
            
    def select_event(self, event_name: str) -> Eventos:
        with DBConnectionHandler() as db:
            data ={    
                db.session
                .query(Eventos)
                .filter(Eventos.nome == event_name)
                .one_or_none() #retorne um ou nenhum
            }
            return data#[0] if data else None #retorna o primeiro elemento do resultado ou None se não encontrar