import streamlit as st
from PIL import Image
import io
import base64
from colorama import init, Fore, Back, Style
import webbrowser
import requests
import folium
import openrouteservice
import pandas as pd
from openrouteservice import Client
from openrouteservice import directions
from geopy.distance import geodesic
from geopy.geocoders import Nominatim


# add kitten logo
icon = Image.open(r'C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\logo_bicimad.png') 

st.set_page_config(page_title="Caso BiciMad, evolución del negocio | By Rubén Carrasco & Juan Lizondo",
                   page_icon=icon,
                   layout="wide",
                   initial_sidebar_state="expanded"
 )     

def get_base64(img_path):
    with open(img_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background(r'C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\fondo_compo_b.png')

# Configuraciones botones:
# Función para cambiar el estilo del botón
# Define un ID único para la columna que contiene los botones
column_id = "mi_columna_con_botones"

# Página Principal
def page_home():
# Dividir la pantalla en dos columnas
    col1, col2 = st.columns([2,  2])
    with col1:
        with st.expander('PREDICCIONES DE MACHINE LEARNING :bulb::'): 
            # Crear un generador para las claves de los botones
            widget_id = (id for id in range(1,  10000))

        # Diccionario con descripciones para cada opción
            descripciones = {
            'Minutos de viaje al mes': '''''',
            'Distancia recorrida al mes': '''''',
            'Bicicletas usadas cada mes': ''''''
            }

        # Crear el selectbox
            prediccion = st.selectbox('',list(descripciones.keys()))
            # Agrupar los botones en un contenedor
            with st.container():
                    # Dividir el contenedor en tres columnas para los botones
                    row1_col1, row1_col2, row1_col3 = st.columns(3)  
                    if prediccion == 'Minutos de viaje al mes':
                        def change_prediction(new_prediction):
                            st.session_state.prediccion = new_prediction
                        if st.button('Decripción del caso', on_click=change_prediction, args=['Decripción del caso']):
                    # Este código se ejecutará cuando se haga clic en el botón
                            pass
                            return st.write(f'''
                                            Este detalle muestra la suma de los tiempos medios de los recorridos en :bike: 🚴‍♂️
                                            de los usuarios por mes. La **inversión** en flota de bicicletas y de estaciones 🏞️
                                            han sido implementadas en nuestro modelo para adecuar la predicción al estado actual de  2024. 📅
                                            Vemos cómo la curva se hace estacionaria en los mismos meses pero 🌈
                                            cómo el tiempo mensual ha crecido exponencialmente. 📈
                                            ''')
                        if row1_col1.button('Predicción 3 meses', key=column_id):
                            minutes3 = Image.open(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\minutes3.png")
                            st.image(minutes3, 'Predicción con valores relativos por límite computacional')
                        if row1_col2.button('Predicción 6 meses', key=column_id + '-btn2'):
                            minutes6 = Image.open(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\minutes6.png")
                            st.image(minutes6, 'Predicción con valores relativos por límite computacional')
                        if row1_col3.button('Predicción de 1 año', key=column_id + '-btn3'):
                            minutes12 = Image.open(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\minutes12.png")
                            st.image(minutes12, 'Predicción con valores relativos por límite computacional')
                    
                    elif prediccion == 'Distancia recorrida al mes':
                        def change_prediction(new_prediction):
                            st.session_state.prediccion = new_prediction
                        if st.button('Decripción del caso', on_click=change_prediction, args=['Decripción del caso']):
                    # Este código se ejecutará cuando se haga clic en el botón
                            pass
                            return st.write('''🚴 Este detalle muestra la suma de las distancias medias de los recorridos en bicicleta 🚴
                                            de los usuarios por mes. La **inversión** en flota de bicicletas y estaciones 🏞️
                                            han sido consideradas en nuestro modelo para adaptar la predicción a la situación actual 📆
                                            de  2024. Al igual que con los minutos, la curva sube creciendo en datos ⬆️
                                            pero con la particularidad de incrementar las distancias entre estaciones. 🔄'''
                                            )
                        if row1_col1.button('Predicción 3 meses', key=next(widget_id)):
                            distance3 = Image.open(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\distance3.png")
                            st.image(distance3, 'Predicción con valores relativos por límite computacional')
                        if row1_col2.button('Predicción 6 meses', key=next(widget_id)):
                            distance6 = Image.open(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\distance6.png")
                            st.image(distance6, 'Predicción con valores relativos por límite computacional')
                        if row1_col3.button('Predicción de 1 año', key=next(widget_id)):
                            distance12 = Image.open(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\distance12.png")
                            st.image(distance12, 'Predicción con valores relativos por límite computacional')

                    elif prediccion == 'Bicicletas usadas cada mes':
                        def change_prediction(new_prediction):
                            st.session_state.prediccion = new_prediction
                        if st.button('Decripción del caso', on_click=change_prediction, args=['Decripción del caso']):
                    # Este código se ejecutará cuando se haga clic en el botón
                            pass
                            return st.write('''
                                            :bicyclist::bicyclist: Este detalle muestra la suma total de :bike: de los usuarios por mes.  
                                            En este caso, hemos utilizado los datos absolutos que disponíamos 📊 y añadido la nueva flota de bicicletas 🚲 de  2023.  
                                            Vemos cómo la predicción hace prácticamente un calco de la curva de los datos obtenidos en  2022 📈, siendo la predicción menos comprometida de nuestro modelo. :mag_right:
                                            ''')
                        if row1_col1.button('Predicción 3 meses', key=next(widget_id)):
                            bikes3 = Image.open(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\bikes3.png")
                            st.image(bikes3, caption='Predicción con valores absolutos sin límite computacional')
                        if row1_col2.button('Predicción 6 meses', key=next(widget_id)):
                            bikes6 = Image.open(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\bikes6.png")
                            st.image(bikes6, caption='Predicción con valores absolutos sin límite computacional')
                        if row1_col3.button('Predicción de 1 año', key=next(widget_id)):
                            bikes12 = Image.open(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\bikes12.png")
                            st.image(bikes12, caption='Predicción con valores absolutos sin límite computacional')
                    
    with col2:
        with st.expander('MEJORAS EN LA USABILIDAD DE LA APP BiciMad :world_map::'): 
            # Diccionario con descripciones para cada opción
            implementos = {
            'Gamificación y usabilidad de la APP': '''Mediante esta implemantación, mejoramos la usabilidad de acceso,
            ruta personalizada e introducimos una gamificación para el usuario.''',
            }

        # Crear el selectbox
            prediccion = st.selectbox('',list(implementos.keys()))

            # Agrupar el botón en un contenedor
            with st.container(): 
                def change_prediction(new_prediction):
                            st.session_state.prediccion = new_prediction
                if st.button('Explicación', on_click=change_prediction, args=['Decripción del caso']):
                    # Este código se ejecutará cuando se haga clic en el botón
                    pass
                    return st.markdown('''
                                        Hemos trabajado en unas mejoras en la usabilidad de la aplicación de BiciMad:

                                        - Por un lado, obtener una puntuación en base al uso que haces de las bicicletas 🚴‍♂️🚲
                                        - Por otro, mejorar la precisión de la ubicación, por proximidad a tu estación de biciMAD 📍🛡️

                                        Estas ideas, nacen del estudio de los datos y de la elaboración del trabajo como propuestas a valorar para el gestor 📊💼
                                        ''')
                # Mostrar el botón:
                if prediccion == 'Gamificación y usabilidad de la APP':
                     # Define a session state variable to track if the button has been clicked
                    if 'button_clicked' not in st.session_state:
                        st.session_state.button_clicked = False

                    # Function to handle the button click
                    def handle_button_click():
                        st.session_state.button_clicked = True

                    # Create the button and associate it with the click handler
                    if st.button('Prueba el uso', on_click=handle_button_click):
                        pass  # Handle the button click event here

                            # Initialize ORS client
                        ors_client = Client(key='5b3ce3597851110001cf6248b1eae734bbbd486a9454e8190d51e71b')
                        
                        # Definimos los límites de Madrid
                        madrid_bounds = {'west': -3.889004, 'south': 40.312071, 'east': -3.518011, 'north': 40.643523}

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
                                address = input("Ingrese su dirección: ")
                                geolocator = Nominatim(user_agent="geo_locator")
                                location = geolocator.geocode(address)

                                if location and madrid_bounds['west'] <= location.longitude <= madrid_bounds['east'] and madrid_bounds['south'] <= location.latitude <= madrid_bounds['north']:
                                    return location.latitude, location.longitude, address
                                else:
                                    print("La dirección proporcionada no está en Madrid. Intente nuevamente.")
                        # def get_nearest_bike_station(user_location, station_data):
                        def get_nearest_bike_station(user_location, station_data):
                            # Convertir las coordenadas de usuario a números flotantes si son cadenas
                            user_location_coords = tuple(map(float, user_location))
                            
                            # Calcular la distancia entre el usuario y cada estación
                            distances = [(geodesic(user_location_coords, (float(station['latitude']), float(station['longitude']))).km, station) for station in station_data]
                            
                            # Ordenar las estaciones por distancia y seleccionar la más cercana
                            nearest_station = min(distances, key=lambda x: x[0])[1]
                            
                            return nearest_station

                            # return min(station_data, key=lambda station: geodesic(user_location[:2], (station['latitude'], station['longitude'])).kilometers)
                
                            # Cargamos el DataFrame con los datos reales
                        data_series = pd.read_csv(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\interim\bicimad_time_series.csv", sep=',')

                            # Asegúrate de ajustar el nombre de las columnas según tus datos reales
                        station_data = [create_station_data(row) for _, row in data_series.iterrows() if create_station_data(row)]

                        def get_route_and_score(start_lat, start_lon, end_lat, end_lon):
                                            # Get the route using ORS
                            route = ors_client.directions([(start_lon, start_lat), (end_lon, end_lat)], profile='cycling-regular')
                                            
                                            # Calculate the distance of the route
                            distance = route['routes'][0]['summary']['distance'] /  1000  # Convert to kilometers
                                            
                                            # Calculate carbon emission and calories burned
                            emission_savings, calories_kcal = calculate_carbon_emission_and_calories(distance, 'bicycle')
                                            
                                            # Calculate score based on distance and emission savings
                            score = int(distance) + int(emission_savings)
                                            
                            return route, score

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

                            # Streamlit app
                    def main():
                            # Input fields for start and destination                  
                        start_address = st.text_input("¿Dónde estoy?") 
                        end_address = st.text_input("¿A dónde voy?")
                        nearest_station_in = get_nearest_bike_station(start_address, station_data)
                        nearest_station_out = get_nearest_bike_station(end_address, station_data)

                        if start_address and end_address:
                                        # Geocode the addresses
                            start_geocode_result = ors_client.pelias_search(text=start_address)
                            end_geocode_result = ors_client.pelias_search(text=end_address)
                                                        
                            if start_geocode_result['type'] == 'FeatureCollection' and len(start_geocode_result['features']) >  0 and \
                                end_geocode_result['type'] == 'FeatureCollection' and len(end_geocode_result['features']) >  0:
                                                            
                                start_coords = start_geocode_result['features'][0]['geometry']['coordinates']
                                end_coords = end_geocode_result['features'][0]['geometry']['coordinates']

                            # Get the route and calculate score
                                route, score = get_route_and_score(*start_coords, *end_coords)                                                       
                            # Display route and score
                                st.write(f"Ruta desde {start_address} hasta {end_address}:")
                                st.write(f"Dirígete desde la estacio: {nearest_station_in} hasta la estación: {nearest_station_out}:")
                                st.map(nearest_station_in, nearest_station_out)
                                #st.map(route['routes'][0]['geometry']['coordinates'])
                                st.write(f'''Tu puntuación es: ¡¡¡{score}!!!:clap::clap::clap::clap::clap:, 
                                        esto es gracias a las calorías gastadas por la velocidad en que 
                                        lo has hecho, y por la distancia recorriday también por tu 
                                        contribución al ahorro de emisiones en nuestra ciudad
                                        por usar la bicicleta :smiley: ''')

                            else:
                                st.error("No se pudieron geocodificar las direcciones. Por favor, inténtalo de nuevo.")

                    if __name__ == "__main__":
                        main()

# Información Adicional
def page_info():
    col1, col2 = st.columns([2,  2])
    with col1:
        with st.expander('Acerca del proyecto sobre BiciMAD :bike:'):
            proyecto = Image.open(r'C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\Proyecto.png')
            st.image(proyecto, use_column_width=True)
        with st.expander('Conclusiones del proyecto :waving_white_flag:'):
            st.write('''🚴‍♂️ Dada la situación actual de monopolio de BiciMad en la red de alquiler
                      de bicicletas de la ciudad, es razonable esperar que los datos de crecimiento
                      que hemos obtenido sean muy positivos. 📈''')
            st.write('''🔍 El modelo respalda esta tendencia empresarial y puede garantizar que, sin
                      tener en cuenta solo ganancias y sin conocer los costos de implementación, 
                     cualquier mejora que pueda aportar este servicio resultará en un crecimiento 
                     exponencial de los datos. 🚀''')

           
    with col2:
        with st.expander('Acerca del modelo de Machine Learning :bookmark_tabs:'):
            st.write('''*Después de analizar el problema comercial 🧩 y estipular que 
                     éste sería una cuestión de series temporales, estudiamos todas las
                      posibilidades de los modelos aprendidos:*''') 
            st.write('''*ARIMA, XGBoost, SVG,... tanto modelos univariantes como multivariantes*.*''') 
            st.write('''***Finalmente y tras varias métricas y evaluaciones, 
                     obtuvimos mejores resultados para una red neuronal basada en el LSTM 🧠.***''') 
            st.write('''*Las Unidades de Memoria a Largo Plazo (LSTM, por sus siglas en inglés) 
                     son una arquitectura de red neuronal diseñada para superar el problema 
                     de "desvanecimiento del gradiente" 🔄, que limita la capacidad para 
                     aprender dependencias a largo plazo. Las LSTM introducen una celda de 
                     memoria que puede mantener u olvidar información a largo plazo, y ésta 
                     celda se actualiza con cada paso temporal en la secuencia. Nuestros 
                     resultados mejoraron significativamente gracias a esta implementación 📈.*''')
        with st.expander('Limitaciones y procesos de mejora :point_up_2:'):
            st.write("""*Uno de los mayores inconvenientes con el procesamiento de los datos,  
            ha sido la imposibilidad de poder limpiar y mergear datos relativos a la  
            información de las estaciones, por lo que hemos podido averiguar, han limitado
            la información que sí ofrecían años atrás.* ⚠️""")

            st.write("""Otro de los problemas más importantes es que los datos referidos a todo el año
            2022, suponían una carga de casi  4 millones y medio de filas, lo que ha conllevado
            en nuestra limitación computacional, a tener que seleccionar una muestra más pequeña
            de nuestro conjunto*.* 📊""")

            st.write("""***Este proyecto tiene mucho margen de mejora si solventamos, con tiempo, nuestras
            limitaciones antes referidas. En una versión  2.0 del proyecto, la demanda de localización
            de estaciones y de bicicletas supondrá una predicción muy interesante para analizar.*** 🚀""")

            st.write("""Otro de los aspectos interesantes de poder predecir y analizar, son los costos operativos.
            Si consiguieramos información adicional de la inversión de bicicletas, estaciones, personal y
            demás indicadores económicos del negocio, podríamos retornar y aventurarnos a ofrecer visiones
            de negocio a futuro.* 💰📈""")
 

    # Selección de la página a mostrar
pages = {
        "Despliegue": page_home,
        "Proyecto": page_info,
    }
logo = Image.open(r'C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\Logo_Bicimad_-_EMT.png')
st.sidebar.image(logo)
st.sidebar.header("Proyecto BiciMad :bike:")
# st.sidebar.text("*Rubén Carrasco")
# linkedin_icon_url = Image.open(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\linkedin.png")
# linkedin_profile_url = "https://www.linkedin.com/in/rub%C3%A9n-carrasco-143145135/"
# with st.sidebar:
#         st.markdown(f"[![LinkedIn]({linkedin_icon_url})]({linkedin_profile_url})", unsafe_allow_html=True)
def load_image(file_path):
    with Image.open(file_path) as img:
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str
linkedin_icon_path = r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\linkedin.png"
linkedin_icon_base64 = load_image(linkedin_icon_path)
linkedin_profile_url_juan = "https://www.linkedin.com/in/juanlizondo/"
linkedin_profile_url_ruben = "https://www.linkedin.com/in/juanlizondo/"
with st.sidebar:
    st.markdown(
        f"""***Rubén Carrasco*** 
        <a href="{linkedin_profile_url_ruben}" target="_blank">
            <img src="data:image/png;base64,{linkedin_icon_base64}" alt="LinkedIn Icon" width="15px" height="15px"/>
        </a>
        """,
        unsafe_allow_html=True
    )
with st.sidebar:
    st.markdown(
        f"""***Juan Lizondo*** 
        <a href="{linkedin_profile_url_juan}" target="_blank">
            <img src="data:image/png;base64,{linkedin_icon_base64}" alt="LinkedIn Icon" width="15px" height="15px"/>
        </a>
        """,
        unsafe_allow_html=True
    )
selection = st.sidebar.radio("***Páginas***", list(pages.keys()))
# Llamada a la función correspondiente a la selección
pages[selection]()