import requests


response = requests.get(f"https://pokeapi.co/api/v2/pokemon/15")
data = response.json()
data_type = data['types'] # Supondo que data é o dicionário com os dados
types_list = []
for type_info in data_type:
    types_list.append(type_info['type']['name'])
types = ', '.join(types_list)
print(data['name'], types)

