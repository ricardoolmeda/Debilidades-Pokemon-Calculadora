# Jugando con mi primera API

# Importamos la libreria requests
import requests
import my_module
import matplotlib.pyplot as plt
from urllib.request import urlopen
from PIL import Image

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
# pokemon = "pikachu" # prueba para no estar siempre con el imput

respuesta = requests.get(URL + pokemon)

datos = respuesta.json()
# print(datos) # Para ver todos los datos que hay

# Para cargar imagenes imagen
url_image = datos["sprites"]["other"]["official-artwork"]["front_default"]

# Queremos mostrar la imagen
print("------------Imagen:------------")

im = Image.open(urlopen(url_image))
plt.imshow(im)
plt.show()


# Queremos que lo muestre el tipo o tipos del pokemon
# Para ello creamos una lista vacía para almacenar los tipos del pokemon
tipo_elegido = []

# Creamos el bucle for :
print(f"------------Tipo de {pokemon}:------------")

for types in datos["types"]:
    tipo = types["type"]["name"]
    tipo_elegido.append(tipo)
    print(tipo)

# print("Estos son los tipos pokemons guardados en la variable: ", tipo_elegido) # esto es porque estoy probando la difencia entre .expend y .append y asi tambien saber si lo guarda.

# Con el modulo que hemos creado vamos a añadir el tipo de daño que hace

def info_damage(tipos):
    combined_types = {}

    for tipo in tipos:
        if tipo in my_module.info_types:
            for atack_type, multiplicator in my_module.info_types[tipo].items():
                if atack_type in combined_types:
                    combined_types[atack_type] *= multiplicator
                else:
                    combined_types[atack_type] = multiplicator

    super_effective_4x = []
    super_effective_2x = []
    normal_1x = []
    not_effective_05x = []
    inmune = []

    for atack_type, value in combined_types.items():
        if value == 4:
            super_effective_4x.append((atack_type, value))
        elif value == 2:
            super_effective_2x.append((atack_type, value))
        elif value == 1:
            normal_1x.append((atack_type, value))
        elif value == 0.5:
            not_effective_05x.append((atack_type, value))
        else:
            inmune.append((atack_type, value))

    return super_effective_4x, super_effective_2x, normal_1x, not_effective_05x, inmune

super_effective_4x, super_effective_2x, normal_1x, not_effective_05x, inmune = info_damage(tipo_elegido)

# Ejecutamos el codigo

print("------------Super effective 4x:------------")
for atack_type in super_effective_4x:
    print(atack_type[0])
print("------------Super effective 2x:------------")
for atack_type in super_effective_2x:
    print(atack_type[0])
print("------------Normal:------------")
for atack_type in normal_1x:
    print(atack_type[0])
print("------------Not effective 0.5x:------------")
for atack_type in not_effective_05x:
    print(atack_type[0])
print("------------Inmune:------------")
for atack_type in inmune:
    print(atack_type[0])



# Queremos que nos muestre las stats
print("------------Stats:------------")
for stats in datos["stats"]:
    stat_name = stats["stat"]["name"] 
    stat_base = stats["base_stat"]
    print(f"{stat_name}: {stat_base}")
    
# Queremos que nos muestre las habilidades
print("------------Ability:------------")
for abilities in datos["abilities"]:
    abiliies_name = abilities["ability"]["name"] 
    stat_base = stats["base_stat"]
    print(f"{abiliies_name}") 

