# Jugando con mi primera API

# Importamos la libreria requests
import requests

# Creamos la variable URL con nuestro enlace
URL = "https://pokeapi.co/api/v2/pokemon/"

# Llamos a nuestro requests con get para que nos muestre los valores mediante get para que nos lo muestre
# Lo añadimos a la variable response (respuesta para poder utilizar la api)
# response = requests.get(URL)

# Podemos saber si la API tiene algún error https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# print(response) # responde a 200 por lo que la api es aceptable

# Asi podemos ver todo lo que trae la API al ser un archivo .json lo tenemos que indicar para ver lo que trae
# print(response.json())

# A nosotros nos interesa los pokemons filtramos solo los pokemons con un input para que solo nos salga esa

pokemon = input("Escribe un pokemon: ")


respuesta = requests.get(URL + pokemon)

datos = respuesta.json()

# print(datos) # Para ver todos los datos que hay

# Queremos que lo muestre el tipo o tipos del pokemon

# Para ello creamos una lista vacía para almacenar los tipos del pokemon
tipo_elegido = []

# Creamos el bucle for :
print(f"------------Tipo de {pokemon}:------------")

for types in datos["types"]:
    tipo =types["type"]["name"]
    tipo_elegido.append(tipo)
    print(tipo)

# Quiero que me indique las debilidades que tiene el pokemon para ello creamos un diccionario

# Diccionario con fortalezas, debilidades e inmunidades de cada tipo de Pokémon
tipos_pokemons = {
    "Water": {
        "strengths": {"Fire": 2, "Rock": 2, "Ground": 2},
        "weaknesses": {"Electric": 2, "Grass": 2},
        "immunities": []
    },
    "Fire": {
        "strengths": {"Grass": 2, "Ice": 2, "Bug": 2, "Steel": 2},
        "weaknesses": {"Water": 2, "Rock": 2, "Ground": 2},
        "immunities": []
    },
    "Grass": {
        "strengths": {"Water": 2, "Ground": 2, "Rock": 2},
        "weaknesses": {"Fire": 2, "Ice": 2, "Poison": 2, "Flying": 2, "Bug": 2},
        "immunities": []
    },
    "Electric": {
        "strengths": {"Water": 2, "Flying": 2},
        "weaknesses": {"Ground": 2},
        "immunities": []
    },
    "Ice": {
        "strengths": {"Grass": 2, "Ground": 2, "Flying": 2, "Dragon": 2},
        "weaknesses": {"Fire": 2, "Fighting": 2, "Rock": 2, "Steel": 2},
        "immunities": []
    },
    "Ground": {
        "strengths": {"Fire": 2, "Electric": 2, "Poison": 2, "Rock": 2, "Steel": 2},
        "weaknesses": {"Water": 2, "Ice": 2, "Grass": 2},
        "immunities": ["Electric"]
    },
    "Ghost": {
        "strengths": {"Ghost": 2, "Psychic": 2},
        "weaknesses": {"Ghost": 2, "Dark": 2},
        "immunities": ["Normal", "Fighting"]
    },
    "Normal": {
        "strengths": {},
        "weaknesses": {"Fighting": 2},
        "immunities": ["Ghost"]
    }
}


# print("Estos son los tipos pokemons guardados en la variable: ", tipo_elegido) # esto es porque estoy probando la difencia entre .expend y .append y asi tambien saber si lo guarda.
