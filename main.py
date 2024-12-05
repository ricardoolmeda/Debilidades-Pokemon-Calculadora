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


print(f"------------Super effective 4x:------------")
for atack_type in super_effective_4x:
    print(atack_type)
print(f"------------Super effective 2x:------------")
for atack_type in super_effective_2x:
    print(f"{atack_type}")
print(f"------------Normal:------------")
for atack_type in normal_1x:
    print(f"{atack_type}")
print(f"------------Not effective 0.5x:------------")
for atack_type in not_effective_05x:
    print(f"{atack_type}")
print(f"------------Inmune:------------")
for atack_type in inmune:
    print(f"{atack_type} ")
