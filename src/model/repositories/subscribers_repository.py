from src.model.configs.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
from .interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
    def insert(self, subscriber_info: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscribers = Inscritos(
                    nome = subscriber_info.get("nome"),
                    email = subscriber_info.get("email"),
                    link = subscriber_info.get("link"),
                    evento_id = subscriber_info.get("evento_id"),
                    
                    )
                db.session.add(new_subscribers) #adicionei para a minha sessão um novo evento
                db.session.commit()

            except Exception as exception:
                db.session.rollback() # se deu certo eu dou um commit, se cair na excessão, rollback e raise da exceção
                raise exception
    def select_subscriber(self, email: str, event_id: int) -> Inscritos:
        with DBConnectionHandler() as db:
            data = ( 
                db.session
                .query(Inscritos)
                .filter(
                    Inscritos.email == email,
                    Inscritos.evento_id == event_id
                    )
                .one_or_none() #retorne um ou nenhum
            )
            return data#[0] if data else None #retorna o primeiro elemento do resultado ou None se não encontrar
    