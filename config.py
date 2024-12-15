# Jugando con mi primera API

# Importamos la libreria requests
import requests
import my_module
from urllib.request import urlopen
from PIL import Image

# Creamos la variable URL con nuestro enlace
URL = "https://pokeapi.co/api/v2/pokemon/"


# Creamos la función para obtener los datos de los pokemons
def obtener_datos_pokemon(pokemon):      
    try: 
        respuesta = requests.get(URL + pokemon) # Llamos a nuestro requests con get para que nos muestre los valores mediante get para que nos lo muestre
        respuesta.raise_for_status()
        pokemon_data = respuesta.json() 
        return pokemon_data # Podemos saber si la API tiene algún error https://developer.mozilla.org/en-US/docs/Web/HTTP/Statusp
    except requests.exceptions.HTTPError: 
        print("Error: El Pokémon no existe. Por favor, introduce un nombre válido.")
        return None
    except Exception as e:
        print(f"Error al obtener los datos del Pokémon: {e}")
        return None

# Mostrar imagen
def mostrar_imagen(imagen):
    try:
        url_image = imagen["sprites"]["other"]["official-artwork"]["front_default"]
        im = Image.open(urlopen(url_image))
        im.show()

    except Exception as e:
        print(f"Error al obtener la imagen del Pokémon: {e}")
        return []
    
# Mostramos Stats
def mostrar_stats(stats):
    try:
        print("------------Stats:------------")
        for stat in stats["stats"]:
            stat_name = stat["stat"]["name"] 
            stat_base = stat["base_stat"]
            print(f"{stat_name}: {stat_base}")

    except Exception as e:
        print(f"Error al obtener las stats del Pokémon: {e}")
        return []    

# Mostramos las abilidades
def mostrar_ability(ability):
    try: 
        print("------------Ability:------------")
        for abilities in ability["abilities"]:
            abiliies_name = abilities["ability"]["name"] 
            print(f"{abiliies_name}") 

    except Exception as e:
        print(f"Error al obtener las abilidades del Pokémon: {e}")
        return []

# Mostramos los tipos
def mostrar_tipos(types):
    try:
        tipos = [tipo["type"]["name"] for tipo in tipos["types"]]
        print(f"------------Tipos de {types['name']}:------------")
        for tipo in tipos:
            print(tipo)
           
    except Exception as e:
        print(f"Error al obtener los tipos del Pokémon: {e}")
        return []
    

def info_damage(tipos):
    
        combined_types = {}

        tipos = [tipo["type"]["name"] for tipo in tipos["types"]]
        
        for tipo in tipos:
            if tipo in my_module.info_types: # Lo que hace es llamar al modelo donde esta los tipos de daño
                for atack_type, multiplicator in my_module.info_types[tipo].items(): # Creamos un bucle para que repita las combincaciones posibles
                    if atack_type in combined_types:
                        combined_types[atack_type] *= multiplicator # Si los tipos se repiten se multiplican
                    else:
                        combined_types[atack_type] = multiplicator

        categorias = {  # Son todas las confinaciones de daño que hay 
            "super_effective_4x": [], 
            "super_effective_2x": [], 
            "normal_1x": [], 
            "not_effective_05x": [], 
            "inmune": [] }
                

        for atack_type, value in combined_types.items(): # Retornamos el bucle para que sumen todos los tipos de daño
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

def mostrar_damage(tipos):
    categorias = info_damage(tipos)
    print("------------Debilidades del pokemon:------------")
    for categoria in categorias:
        print(f"-----{categoria}-----")
        for atack_type in categorias[categoria]:
            print(atack_type[0])




    




# Creamos la función para que funcione el programa
def main():
    while True:
        pokemon = input("Escribe un pokemon :").lower()
        datos = obtener_datos_pokemon(pokemon)
        if datos:
                mostrar_imagen(datos)
                mostrar_stats(datos)
                mostrar_ability(datos)
                mostrar_tipos(datos)
                mostrar_damage(datos)

        
        comparar_otro = input("\n¿Quieres comparar otro Pokémon? (si/no): ").lower() 
    
        if comparar_otro == "no":
            print("-----Perfecto vuelve a ejecutar si quieres saber más----")
            return
        elif comparar_otro != "si": 
            print("---Has puesto mal el nombre del pokemon vuelve a ejecutar el programa")
            break    
            

if __name__=="__main__":
    main()




