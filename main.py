# Jugando con mi primera API

# Importamos la libreria requests
import requests
import my_module
import matplotlib.pyplot as plt
from urllib.request import urlopen
from PIL import Image

# Creamos la variable URL con nuestro enlace
URL = "https://pokeapi.co/api/v2/pokemon/"


# Creamos la función para obtener los datos de los pokemons
def obtener_datos_pokemon(pokemon):      
    try: 
        respuesta = requests.get(URL + pokemon) # Llamos a nuestro requests con get para que nos muestre los valores mediante get para que nos lo muestre
        respuesta.raise_for_status() 
        return respuesta.json() # Podemos saber si la API tiene algún error https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    except requests.exceptions.HTTPError: 
        print("Error: El Pokémon no existe. Por favor, introduce un nombre válido.")
        return None

# Asi podemos ver todo lo que trae la API al ser un archivo .json lo tenemos que indicar para ver lo que trae
# print(response.json())

# pokemon = "pikachu" # prueba para no estar siempre con el input
# print(datos) # Para ver todos los datos que hay

# Creamos la funcion para mostrar la imagen
def mostar_imagen(url_image):
    im = Image.open(urlopen(url_image))
    plt.imshow(im)
    plt.show()

# Creamos la funcion para obtener los tipos del pokemon
def obtener_tipos(datos):
   tipos = [tipo["type"]["name"] for tipo in datos["types"]] 
   return tipos

# Creamos la funcion de daños
def info_damage(tipos):
    combined_types = {}

    for tipo in tipos:
        if tipo in my_module.info_types:
            for atack_type, multiplicator in my_module.info_types[tipo].items():
                if atack_type in combined_types:
                    combined_types[atack_type] *= multiplicator
                else:
                    combined_types[atack_type] = multiplicator

    categorias = { 
        "super_effective_4x": [], 
        "super_effective_2x": [], 
        "normal_1x": [], 
        "not_effective_05x": [], 
        "inmune": [] }
            

    for atack_type, value in combined_types.items():
        if value == 4:
            categorias["super_effective_4x"].append((atack_type, value))
        elif value == 2:
            categorias["super_effective_2x"].append((atack_type, value))
        elif value == 1:
            categorias["normal_1x"].append((atack_type, value))
        elif value == 0.5:
            categorias["not_effective_05x"].append((atack_type, value))
        else:
            categorias["inmune"].append((atack_type, value))

    return categorias

def mostrar_informacion_pokemon(datos):
    # Mostramos la imagen
    url_image = datos["sprites"]["other"]["official-artwork"]["front_default"] # Para cargar la imagen
    print("------------Imagen:------------")
    mostar_imagen(url_image)

    # Mostramos el tipo del pokemon
    tipos = obtener_tipos(datos)
    print(f"------------Tipos de {datos['name']}:------------")
    for tipo in tipos:
        print(tipo)
    
    # Mostramos debilidades
    categorias = info_damage(tipos)
    print("------------Debilidades del pokemon:------------")
    print("------------Super effective 4x:------------")
    for atack_type in categorias["super_effective_4x"]:
        print(atack_type[0])
    print("------------Super effective 2x:------------")
    for atack_type in categorias["super_effective_2x"]:
        print(atack_type[0])
    print("------------Normal:------------")
    for atack_type in categorias["normal_1x"]:
        print(atack_type[0])
    print("------------Not effective 0.5x:------------")
    for atack_type in categorias["not_effective_05x"]:
        print(atack_type[0])
    print("------------Inmune:------------")
    for atack_type in categorias["inmune"]:
        print(atack_type[0])

    # Mostramos las Stats
    print("------------Stats:------------")
    for stats in datos["stats"]:
        stat_name = stats["stat"]["name"] 
        stat_base = stats["base_stat"]
        print(f"{stat_name}: {stat_base}")
    
    # Mostramos las abilidades
    print("------------Ability:------------")
    for abilities in datos["abilities"]:
        abiliies_name = abilities["ability"]["name"] 
        stat_base = stats["base_stat"]
        print(f"{abiliies_name}") 

# Creamos la función para que funcione el programa
def main():
    while True:
        pokemon = input("Escribe un pokemon :").lower()
        datos = obtener_datos_pokemon(pokemon)
        if datos:
                mostrar_informacion_pokemon(datos)
        
        comparar_otro = input("\n¿Quieres comparar otro Pokémon? (si/no): ").lower() 
    
        if comparar_otro != "si":
            print("-----Perfecto vuelve a ejecutar si quieres saber más----")
            break            
            

if __name__=="__main__":
    main()