# Jugando con mi primera API

# Importamos la libreria requests
import requests
import my_module

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

# print("Estos son los tipos pokemons guardados en la variable: ", tipo_elegido) # esto es porque estoy probando la difencia entre .expend y .append y asi tambien saber si lo guarda.

