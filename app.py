import streamlit as st
from PIL import Image
import base64
from colorama import init, Fore, Back, Style
import webbrowser
import requests
import folium
import openrouteservice


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
                            return st.write('''Este detalle muestra la suma de los tiempos medios de los recorridos en :bike:
                                            de los usuarios por mes. La ***inversión*** de flota de bicicletas y de estaciones 
                                            han sido implementadas en nuestro modelo para adecuar la prediccióna la situación 
                                            actual de 2024. Vemos como la curva se hace estacionaria en los mismos meses pero
                                            cómo el tiempo mensual ha crecido exponencialmente.''')
                        if row1_col1.button('Predicción 3 meses', key=column_id):
                            st.image(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\minutes3.png", 
                                    caption='Predicción con valores relativos por límite computacional')
                        if row1_col2.button('Predicción 6 meses', key=column_id + '-btn2'):
                            st.image(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\minutes6.png", 
                                    caption='Predicción con valores relativos por límite computacional')
                        if row1_col3.button('Predicción de 1 año', key=column_id + '-btn3'):
                            st.image(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\minutes12.png", 
                                    caption='Predicción con valores relativos por límite computacional')
                    
                    elif prediccion == 'Distancia recorrida al mes':
                        def change_prediction(new_prediction):
                            st.session_state.prediccion = new_prediction
                        if st.button('Decripción del caso', on_click=change_prediction, args=['Decripción del caso']):
                    # Este código se ejecutará cuando se haga clic en el botón
                            pass
                            return st.write('''Este detalle muestra la suma de las distancias medias de los recorridos en :bike:
                                            de los usuarios por mes. La ***inversión*** de flota de bicicletas y de estaciones 
                                            han sido implementadas en nuestro modelo para adecuar la predicción a la situación actual
                                            de 2024. Al igual que en el caso de los minutos, la curva se repie creciendo en datos
                                            pero con la distinción de incrementar las distancias entre estaciones.''')
                        if row1_col1.button('Predicción 3 meses', key=next(widget_id)):
                            st.image(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\distance3.png", 
                                    caption='Predicción con valores relativos por límite computacional')
                        if row1_col2.button('Predicción 6 meses', key=next(widget_id)):
                            st.image(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\distance6.png", 
                                    caption='Predicción con valores relativos por límite computacional')
                        if row1_col3.button('Predicción de 1 año', key=next(widget_id)):
                            st.image(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\distance12.png", 
                                    caption='Predicción con valores relativos por límite computacional')
                    
                    elif prediccion == 'Bicicletas usadas cada mes':
                        def change_prediction(new_prediction):
                            st.session_state.prediccion = new_prediction
                        if st.button('Decripción del caso', on_click=change_prediction, args=['Decripción del caso']):
                    # Este código se ejecutará cuando se haga clic en el botón
                            pass
                            return st.write('''Este detalle muestra la suma total de :bike: de los usuarios por mes. En este caso, 
                                            hemos utilizado los datos absolutos que disponíamos y añadido la nueva flota de bicicletas
                                            de 2023. Vemos como la predicción hace practicamente un calco de la curva de los datos 
                                            obtenidos en 2022, siendo la predicción menos comprometida de nuestro modelo. ''')
                        if row1_col1.button('Predicción 3 meses', key=next(widget_id)):
                            st.image(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\bikes3.png", 
                                    caption='Predicción con valores absolutos sin límite computacional')
                        if row1_col2.button('Predicción 6 meses', key=next(widget_id)):
                            st.image(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\bikes6.png", 
                                    caption='Predicción con valores absolutos sin límite computacional')
                        if row1_col3.button('Predicción de 1 año', key=next(widget_id)):
                            st.image(r"C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\bikes12.png", 
                                    caption='Predicción con valores absolutos sin límite computacional')
                    
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
                # Mostrar el botón:
                if prediccion == 'Gamificación y usabilidad de la APP':
                        def change_prediction(new_prediction):
                            st.session_state.prediccion = new_prediction
                        if st.button('Explicación', on_click=change_prediction, args=['Decripción del caso']):
                    # Este código se ejecutará cuando se haga clic en el botón
                            pass
                            return st.write('''Hemos trabajado en unas mejoras en la usabilidad de la aplicación
                                        de BiciMad para el usuario, obtener una puntuación y meorar la preción 
                                        la ubicación, nacen cómo propuestas a valorar para el gestor.''')
                        if st.button('Prueba el uso'):
                            ors_client = openrouteservice.Client(key='5b3ce3597851110001cf6248b1eae734bbbd486a9454e8190d51e71b')

                            def get_user_location():
                                address = st.text_input("¿Dónde estoy?")
                                if address:
                                    # Geocodifica la dirección ingresada por el usuario
                                    geocode_result = ors_client.pelias_search(text=address)
                                    if geocode_result['type'] == 'FeatureCollection' and geocode_result['features']:
                                        location = geocode_result['features'][0]['geometry']['coordinates']
                                        return location[1], location[0], address
                                    else:
                                        st.error("No se pudo geocodificar la dirección. Por favor, inténtalo de nuevo.")
                                else:
                                    st.warning("Por favor, ingrese una dirección válida.")

                # Ejemplo de uso en tu aplicación Streamlit
                            user_location = get_user_location()
                            if user_location:
                            # Aquí puedes usar user_location para calcular la ruta óptima
                                st.success(f"La ubicación del usuario es: {user_location}")

# Información Adicional
def page_info():
    st.title("BiciMad - Conoce más sobre el proyecto")
    st.write("Aquí encontrará más detalles sobre el proyecto.")

# Selección de la página a mostrar
pages = {
    "Despliegue": page_home,
    "Proyecto": page_info,
}

st.sidebar.image(r'C:\Users\LuyinPC\Desktop\Bici-Mad\BiciMad_4geeks_ML\BiciMad_4geeks_ML\data\graficos\images\Logo_Bicimad_-_EMT.png')
selection = st.sidebar.radio("Páginas", list(pages.keys()))
# Llamada a la función correspondiente a la selección
pages[selection]()
st.sidebar.title("Proyecto BiciMad :bike:")
st.sidebar.header("*Rubén Carrasco *Juan Lizondo")
with st.sidebar:
     #if st.button('Acerca del modelo de Machine Learning'):
        with st.expander('Acerca del modelo de Machine Learning'):
            st.write('''*Despues de analizar el problema comercial y estipular que éste sería una 
            cuestión de series temporales, estudiamos todas las posibilidades: ARIMA, XGBoost
            , SVG,... tando modelos univariantes como multivariantes. Finalmente y tras 
            varias métricas y evaluaciones, obtuvimos mejores resultados para una red neuronal basada en el LSTM. 
            Las Unidades de Memoria a Largo Plazo (LSTM, por sus siglas en inglés) son una arquitectura 
            de red neuronal diseñada para superar el problema de "desvanecimiento del gradiente", 
            que limita la capacidad para aprender dependencias a largo plazo. 
            Las LSTM introducen una celda de memoria que puede mantener u olvidar información a largo plazo, 
            y ésta celda se actualiza con cada paso temporal en la secuencia.*''')
            
