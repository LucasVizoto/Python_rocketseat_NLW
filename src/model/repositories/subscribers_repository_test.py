from .subscribers_repository import SubscribersRepository
import pytest

@pytest.mark.skip("Insert in DB")
def test_inser():
    subscriber_info = {
        "nome" : "Beatriz",
        "email" : "bia@example.com",
        "evento_id": 1
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "bia@exemplo.com"
    evento_id = 2

    subs_repo = SubscribersRepository()
    subscriber = subs_repo.select_subscriber(email, evento_id)
    print(subscriber.nome)