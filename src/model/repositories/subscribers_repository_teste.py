import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name": "Eduardo Nascimento",
        "email": "eduardonapratica@gmail.com",
        "evento_id": 1
    }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select from DB")
def test_select_subscriber():
    email = "eduardonapratica@gmail.com"
    evento_id = 1
    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email,evento_id)
    print(resp.nome)
