# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
# ---

# +
import streamlit as st
from PIL import Image
import base64
from colorama import init, Fore, Back, Style
import webbrowser
import requests
import folium
from folium import map
import openrouteservice
import pandas as pd
from openrouteservice import Client
from openrouteservice import directions
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import folium
from folium.plugins import PolyLine

#st.button('Prueba el uso')

# Carga el DataFrame con las estaciones de BiciMad
data_series = pd.read_csv(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\interim\bicimad_time_series.csv", sep=',')
# Definimos los límites de Madrid
madrid_bounds = {'west': -3.889004, 'south': 40.312071, 'east': -3.518011, 'north': 40.643523}

# Asegúrate de ajustar el nombre de las columnas según tus datos reales
station_data = [create_station_data(row) for _, row in data_series.iterrows() if create_station_data(row)]

def create_station_data(data_series):
    if madrid_bounds['west'] <= data_series['longitude_unlock'] <= madrid_bounds['east'] and madrid_bounds['south'] <= data_series['latitude_unlock'] <= madrid_bounds['north']:
        return {
            'station_id': data_series['unlock_station_name_n'],
            'latitude': data_series['latitude_unlock'],
            'longitude': data_series['longitude_unlock'],
            'address': data_series['station_unlock']
        }
    else:
        return None

def get_user_location():
    while True:
        address = partida, llegada
        geolocator = Nominatim(user_agent="geo_locator")
        location = geolocator.geocode(address)

        if location and madrid_bounds['west'] <= location.longitude <= madrid_bounds['east'] and madrid_bounds['south'] <= location.latitude <= madrid_bounds['north']:
            return location.latitude, location.longitude, address
        else:
            print("La dirección proporcionada no está en Madrid. Intente nuevamente.")

def get_nearest_station(user_location, station_data):
    return min(station_data, key=lambda station: geodesic(user_location[:2], (station['latitude'], station['longitude'])).kilometers)

# def calcular_ruta_optima(partida, llegada):
#     # Implementa aquí el algoritmo de búsqueda de caminos
#     # y devuelve la ruta óptima y la distancia total
#     pass

# def calcular_puntuacion(distancia, ahorro_co2):
#     # Calcula la puntuación basada en la distancia y el ahorro de CO2
#     distancia = calcular_ruta_optima(distancia_km)
#     ahorro_co2 = distancia
#     puntuacion = distancia + ahorro_co2
#     return puntuacion


def calculate_carbon_emission_and_calories(distance, transportation_mode, fuel_type='gasoline'):
    # Factores de emisión y consumo predefinidos para diferentes modos de transporte y tipos de combustible
    emission_factors = {'bicycle': 0.0, 'bus': 0.1, 'car': {'gasoline': 2.35, 'diesel': 2.64}}
    consumption_factors = {'gasoline': 5.4, 'diesel': 4.8}  # L/100km
    
    emission_factor_car = emission_factors.get('car', {}).get(fuel_type, 0.0)
    emission_factor_bicycle = emission_factors.get('bicycle', 0.0)
    
    # Calcular emisiones de CO2 para automóvil y bicicleta
    total_emission_car = emission_factor_car / 100 * consumption_factors.get(fuel_type, 0.0) * distance
    total_emission_bicycle = emission_factor_bicycle * distance
    
    # Calcular el ahorro de emisiones al usar la bicicleta en lugar del automóvil
    emission_savings = total_emission_car - total_emission_bicycle
    
    # Calcular calorías gastadas (supongamos una velocidad promedio de 20 km/h)
    speed_kmh = 20
    if transportation_mode == 'bicycle':
        if speed_kmh <= 15:
            total_calories = 300 * distance
        elif speed_kmh <= 18:
            total_calories = 420 * distance
        elif speed_kmh <= 22:
            total_calories = 600 * distance
        elif speed_kmh <= 28:
            total_calories = 850 * distance
        else:
            total_calories = 1000 * distance
    else:
        total_calories = 0.0
    
    # Convertir calorías a kilocalorías (1 Cal = 1 kcal)
    total_calories_kcal = total_calories / 1000
    
    return emission_savings, total_calories_kcal

ors_client = Client(key='5b3ce3597851110001cf6248b1eae734bbbd486a9454e8190d51e71b')

partida = get_user_location() 
llegada = get_user_location()

start_lat = get_nearest_station(partida, station_data['latitude'])
start_lon = get_nearest_station(partida, station_data['longitude'])
end_lat = get_nearest_station(llegada, station_data['latitude'])
end_lon = get_nearest_station(llegada, station_data['longitude'])

def get_route_score_and_map(start_lat, start_lon, end_lat, end_lon):
                    # Get the route using ORS
    route = ors_client.directions([(start_lon, start_lat), (end_lon, end_lat)], profile='cycling-regular')
                    
                    # Calculate the distance of the route
    distance = route['routes'][0]['summary']['distance'] /  1000  # Convert to kilometers
                    
                    # Calculate carbon emission and calories burned
    emission_savings, calories_kcal = calculate_carbon_emission_and_calories(distance, 'bicycle')
    calories_kcal = emission_savings # establecemos un rango medio, este dato se debería extraer y cruzar con los datos del perfil del usuario de BiciMad.

                    # Calculate score based on distance and emission savings
    score = int(distance) + int(emission_savings)

    # Suponiendo que 'route' es el objeto obtenido de la API de direcciones
    coordinates = route['routes'][0]['geometry']['coordinates']

    # Crear un mapa centrado en el punto de inicio
    mapa = folium.Map(location=[start_lat, start_lon], zoom_start=13)

    # Trazar la ruta en el mapa
    PolyLine(locations=coordinates, color="blue", weight=2.5).add_to(mapa)
                       
    return route, score, mapa


# Disponibilidad de bicicletas en la estación de salida #
# URL base de la API
base_url = "https://openapi.emtmadrid.es/v1"
email = "ruben.c_ac@icloud.com"
password = "Prada2024!"

token = '27cd5a5c-dc4a-4625-89ee-2b6d3b81880c' #??

def iniciar_sesion(email, password):
    url = f"{base_url}/mobilitylabs/user/login/"
    headers = {
        "email": email,
        "password": password
    }

    response = requests.get(url, headers=headers)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Capturar y devolver el token de acceso
        # token = response.json().get("data", [{}])[0].get("accessToken") # 27cd5a5c-dc4a-4625-89ee-2b6d3b81880c
        return token
    else:
        # Imprimir el código de estado y la respuesta en caso de error
        print("Error en la solicitud de inicio de sesión:")
        print("Código de estado:", response.status_code)
        print("Respuesta:", response.json())
        return None

access_token = token #???

def obtener_estado_estacion_bicimad(access_token, station_data):
    url = f"{base_url}/transport/bicimad/stations/{station_data}/"
    headers = {"accessToken": access_token}

    response = requests.get(url, headers=headers)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Capturar y devolver los detalles de la estación
        estado_estacion = response.json()
        return estado_estacion
    else:
        # Imprimir el código de estado y la respuesta en caso de error
        print("Error en la solicitud de estado de estación BiciMAD:")
        print("Código de estado:", response.status_code)
        print("Respuesta:", response.json())
        return None


# Interfaz de usuario en Streamlit
st.title("Optimizador de Rutas en BiciMad")

# Widgets para ingresar las ubicaciones
partida = st.text_input("¿Dónde estoy?")
llegada = st.text_input("¿A dónde voy?")

# Botón para calcular la ruta
if st.button("Calcular Ruta"):

    # distancia = ???
    route, score, mapa = get_route_score_and_map(start_lat, start_lon, end_lat, end_lon)
    disponibles = obtener_estado_estacion_bicimad(token, station_data)

    st.write(f"Este es tu trayecto:{mapa}")
    st.write(f"La ruta en bicicleta es: {route} y tienes {disponibles} bicicletas en la estación")
    # st.write(f"Distancia recorrida: {distancia} km")
    st.write(f"Puntuación: {score} puntos")



# st.button('Prueba el uso')
#                                 # Streamlit app
# def main(): 
#                                         # Initialize ORS client
#         ors_client = Client(key='5b3ce3597851110001cf6248b1eae734bbbd486a9454e8190d51e71b')
                                    
#                                     # Definimos los límites de Madrid
#         madrid_bounds = {'west': -3.889004, 'south': 40.312071, 'east': -3.518011, 'north': 40.643523}

#         def create_station_data(data_series):
#             if madrid_bounds['west'] <= data_series['longitude_unlock'] <= madrid_bounds['east'] and madrid_bounds['south'] <= data_series['latitude_unlock'] <= madrid_bounds['north']:
#                         return {
#                                                     'station_id': data_series['unlock_station_name_n'],
#                                                     'latitude': data_series['latitude_unlock'],
#                                                     'longitude': data_series['longitude_unlock'],
#                                                     'address': data_series['station_unlock']
#                                                     }
#             else:
#                         return None

#         def get_user_location():
#                     while True:
#                         address = input("Ingrese su dirección: ")
#                         geolocator = Nominatim(user_agent="geo_locator")
#                         location = geolocator.geocode(address)

#                         if location and madrid_bounds['west'] <= location.longitude <= madrid_bounds['east'] and madrid_bounds['south'] <= location.latitude <= madrid_bounds['north']:
#                             return location.latitude, location.longitude, address
#                         else:
#                             print("La dirección proporcionada no está en Madrid. Intente nuevamente.")
#                                     # def get_nearest_bike_station(user_location, station_data):
#         def get_nearest_bike_station(user_location, station_data):
#                                     # Convertir las coordenadas de usuario a números flotantes si son cadenas
#                     user_location_coords = tuple(map(float, user_location))
                                        
#                     # Calcular la distancia entre el usuario y cada estación
#                     distances = [(geodesic(user_location_coords, (float(station['latitude']), float(station['longitude']))).km, station) for station in station_data]
                                        
#                     # Ordenar las estaciones por distancia y seleccionar la más cercana
#                     nearest_station = min(distances, key=lambda x: x[0])[1]
                                        
#                     return nearest_station

#                     # return min(station_data, key=lambda station: geodesic(user_location[:2], (station['latitude'], station['longitude'])).kilometers)
                            
#                     # Cargamos el DataFrame con los datos reales
#         data_series = pd.read_csv(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\interim\bicimad_time_series.csv", sep=',')

#                                         # Asegúrate de ajustar el nombre de las columnas según tus datos reales
#         station_data = [create_station_data(row) for _, row in data_series.iterrows() if create_station_data(row)]

#         def get_route_and_score(start_lat, start_lon, end_lat, end_lon):
#                         # Get the route using ORS
#                     route = ors_client.directions([(start_lon, start_lat), (end_lon, end_lat)], profile='cycling-regular')
                                                        
#                         # Calculate the distance of the route
#                     distance = route['routes'][0]['summary']['distance'] /  1000  # Convert to kilometers
                                                        
#                                                         # Calculate carbon emission and calories burned
#                     emission_savings, calories_kcal = calculate_carbon_emission_and_calories(distance, 'bicycle')
                                                        
#                                                         # Calculate score based on distance and emission savings
#                     score = int(distance) + int(emission_savings)
                                                        
#                     return route, score

#         def calculate_carbon_emission_and_calories(distance, transportation_mode, fuel_type='gasoline'):
#                     # Factores de emisión y consumo predefinidos para diferentes modos de transporte y tipos de combustible
#                     emission_factors = {'bicycle': 0.0, 'bus': 0.1, 'car': {'gasoline': 2.35, 'diesel': 2.64}}
#                     consumption_factors = {'gasoline': 5.4, 'diesel': 4.8}  # L/100km
                                        
#                     emission_factor_car = emission_factors.get('car', {}).get(fuel_type, 0.0)
#                     emission_factor_bicycle = emission_factors.get('bicycle', 0.0)
                                        
#                     # Calcular emisiones de CO2 para automóvil y bicicleta
#                     total_emission_car = emission_factor_car / 100 * consumption_factors.get(fuel_type, 0.0) * distance
#                     total_emission_bicycle = emission_factor_bicycle * distance
                                        
#                     # Calcular el ahorro de emisiones al usar la bicicleta en lugar del automóvil
#                     emission_savings = total_emission_car - total_emission_bicycle
                                        
#                     # Calcular calorías gastadas (supongamos una velocidad promedio de 20 km/h)
#                     speed_kmh = 20
#                     if transportation_mode == 'bicycle':
#                         if speed_kmh <= 15:
#                             total_calories = 300 * distance
#                         elif speed_kmh <= 18:
#                             total_calories = 420 * distance
#                         elif speed_kmh <= 22:
#                             total_calories = 600 * distance
#                         elif speed_kmh <= 28:
#                             total_calories = 850 * distance
#                         else:
#                             total_calories = 1000 * distance
#                     else:
#                         total_calories = 0.0
                                        
#                     # Convertir calorías a kilocalorías (1 Cal = 1 kcal)
#                     total_calories_kcal = total_calories / 1000
                                        
#                     return emission_savings, total_calories_kcal


#                                         # Input fields for start and destination                  
#         start_address = st.text_input("¿Dónde estoy?") 
#         end_address = st.text_input("¿A dónde voy?")

#         if start_address and end_address:
#                     ors_client = Client(key='5b3ce3597851110001cf6248b1eae734bbbd486a9454e8190d51e71b')
#                                                     # Geocode the addresses
#                     start_geocode_result = ors_client.pelias_search(text=start_address)
#                     end_geocode_result = ors_client.pelias_search(text=end_address)
                                                                    
#                     if start_geocode_result['type'] == 'FeatureCollection' and len(start_geocode_result['features']) >  0 and \
#                         end_geocode_result['type'] == 'FeatureCollection' and len(end_geocode_result['features']) >  0:
                                                                        
#                         start_coords = start_geocode_result['features'][0]['geometry']['coordinates']
#                         end_coords = end_geocode_result['features'][0]['geometry']['coordinates']

#                         nearest_station_in = get_nearest_bike_station(start_address, station_data)
#                         nearest_station_out = get_nearest_bike_station(end_address, station_data)
#                                         # Get the route and calculate score
                        
#                         route, score = get_route_and_score(*start_coords, *end_coords)                                                       
#                                         # Display route and score
#                         st.write(f"Ruta desde {start_address} hasta {end_address}:")
#                         st.write(f"Dirígete desde la estacio: {nearest_station_in} hasta la estación: {nearest_station_out}:")
#                         st.map(nearest_station_in, nearest_station_out)
#                         #st.map(route['routes'][0]['geometry']['coordinates'])
#                         st.write(f'''Tu puntuación es: ¡¡¡{score}!!!:clap::clap::clap::clap::clap:, 
#                                                     esto es gracias a las calorías gastadas por la velocidad en que 
#                                                     lo has hecho, y por la distancia recorriday también por tu 
#                                                     contribución al ahorro de emisiones en nuestra ciudad
#                                                     por usar la bicicleta :smiley: ''')

#                     else:
#                         st.error("No se pudieron geocodificar las direcciones. Por favor, inténtalo de nuevo.")

# if __name__ == "__main__":
#     main()
