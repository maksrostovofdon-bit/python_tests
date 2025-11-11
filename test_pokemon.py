import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4208034b7f803e2cca3361a91d0dee3d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 42468

def test_status_code():
    response = requests.get(url= f'{URL}/pokemons',params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url= f'{URL}/pokemons',params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == "tyranitar"

def test_status_code_trainer():
    response_trainers = requests.get(url= f'{URL}/trainers',params={'trainer_id': TRAINER_ID})
    assert response_trainers.status_code == 200

def test_status_code_trainer_d():
    response_trainers_d = requests.get(url= f'{URL}/trainers',params={'trainer_id': TRAINER_ID})
    assert response_trainers_d.json()["data"][0]["trainer_name"] == "Оскар"