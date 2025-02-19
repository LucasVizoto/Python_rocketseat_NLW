# o pytest consegue identificar todo munod que termina com _test
# por isso é possível realizar os testes unitários
# verifica e executa todas as funções com test na frente
from .eventos_repository import EventosRepository
import pytest


@pytest.mark.skip("Insert in DB") #estou pulando o teste e dizendo o pq 
def test_insert_eventos():
    event_name = 'eventoTeste'
    event_repo = EventosRepository()

    event_repo.insert(event_name)

@pytest.mark.skip("Select in DB") #estou pulando o teste e dizendo o pq 
def test_select_events():
        event_name = 'eventoTeste'
        event_repo = EventosRepository()

        event = event_repo.select_event(event_name)
        print(event)
        print(event.name)

# são teste de integração pois estamos testando a conexão com o banco

@pytest.mark.skip("Delete by id in DB") #estou pulando o teste e dizendo o pq 
def test_delete_event():
      event_id = 2
      event_repo = EventosRepository()

      event_repo.delete_event(event_id)