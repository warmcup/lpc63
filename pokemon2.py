# Script en python que consulta el api de pokemon
# para listar los nombres de pokemon pero se le agrego 
# interacción para que listaras más pokemons segun se vaya requiriendo.
# Autor: Juan Ángel Garza Castillo
# Fecha: 9/9/2022
# Matrícula: 2007612

import requests

def get_pokemons(url = 'https://pokeapi.co/api/v2/pokemon-form', offset = 0):
    args = {'offset' : offset} if offset else {}
    respuesta = requests.get(url, params=args)
    if respuesta.status_code == 200:
        resultados = respuesta.json().get('results', [])
        if resultados:
            for pokemon in resultados:
                print(pokemon['name'])
            next = input('¿Continuar listando? [y/n] ').lower()
            if next == 'y':
                get_pokemons(offset=offset+20)

if __name__ == '__main__':
    get_pokemons()
