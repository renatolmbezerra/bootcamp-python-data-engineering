import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True

def pegar_pokemon(id: int) -> PokemonSchema: # Contrato de dados, schema de dados, a view da mimha API
    """
    O objetivo é pegar nome e tipo do pokemon, porém um pokemon pode ter vários
    tipos, por isso será necessário iterar pelos tipos para salvar todos em uma lista
    """
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    data_type = data['types'] # Supondo que data é o dicionário com os dados
    types_list = []
    for type_info in data_type:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name=data['name'], type=types)

if __name__ == "__main__":
    print(pegar_pokemon(10))
    print(pegar_pokemon(6))
    print(pegar_pokemon(13))


# lista_de_alunos = ["kaio", "bruno", "fabio"]
# alunos_string = ', '.join(lista_de_alunos)
# print(alunos_string)

