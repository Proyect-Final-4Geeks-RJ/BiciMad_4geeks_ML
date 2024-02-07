import streamlit as st
from streamlit_extras.app_logo import add_logo
from PIL import Image
import base64

# add kitten logo
icon = Image.open('/workspaces/BiciMad_4geeks_ML/data/graficos/images/logo_bicimad.png') 

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

set_background('/workspaces/BiciMad_4geeks_ML/data/graficos/images/fondo_app.png')

# Configuraciones botones:
# Función para cambiar el estilo del botón
# Define un ID único para la columna que contiene los botones
column_id = "mi_columna_con_botones"

# Crea una columna con el ID definido
col1, _ = st.columns([1,  1])
with col1:
    st.markdown(
        f"""
        <style>
        #{column_id} button {{
            font-size:  2px;
            color-font: #BC3020;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

st.sidebar.image('/workspaces/BiciMad_4geeks_ML/data/graficos/images/logo_bicimad.png')
st.sidebar.header("[**This dashboard app is created by *Rubén Carrasco* & *Juan Lizondo**]")

# Dividir la pantalla en dos columnas
col1, col2 = st.columns([2,  2])
with col1:
    # Crear un generador para las claves de los botones
    widget_id = (id for id in range(1,  10000))

    # Crear un menú desplegable con las opciones
    prediccion = st.selectbox(
        'Selecciona una predicción:',  
        ['Minutos de viaje al mes', 'Distancia recorrida al mes', 'Bicicletas usadas cada mes']
    )  
    # Agrupar los botones en un contenedor
    with st.container():
        # Dividir el contenedor en tres columnas para los botones
        row1_col1, row1_col2, row1_col3 = st.columns(3)  
        # Mostrar los botones solo si la opción correspondiente está seleccionada
        if prediccion == 'Minutos de viaje al mes':
            if row1_col1.button('Predicción 3 meses', key=column_id):
                st.image("/workspaces/BiciMad_4geeks_ML/data/graficos/images/minutes3.png", 
                         caption='Predicción con valores relativos por límite computacional')
            if row1_col2.button('Predicción 6 meses', key=column_id + '-btn2'):
                st.image("/workspaces/BiciMad_4geeks_ML/data/graficos/images/minutes6.png", 
                         caption='Predicción con valores relativos por límite computacional')
            if row1_col3.button('Predicción de 1 año', key=column_id + '-btn3'):
                st.image("/workspaces/BiciMad_4geeks_ML/data/graficos/images/minutes12.png", 
                         caption='Predicción con valores relativos por límite computacional')
        
        elif prediccion == 'Distancia recorrida al mes':
            if row1_col1.button('Predicción 3 meses', key=next(widget_id)):
                st.image("/workspaces/BiciMad_4geeks_ML/data/graficos/images/distance3.png", 
                         caption='Predicción con valores relativos por límite computacional')
            if row1_col2.button('Predicción 6 meses', key=next(widget_id)):
                st.image("/workspaces/BiciMad_4geeks_ML/data/graficos/images/distance6.png", 
                         caption='Predicción con valores relativos por límite computacional')
            if row1_col3.button('Predicción de 1 año', key=next(widget_id)):
                st.image("/workspaces/BiciMad_4geeks_ML/data/graficos/images/distance12.png", 
                         caption='Predicción con valores relativos por límite computacional')
        
        elif prediccion == 'Bicicletas usadas cada mes':
            if row1_col1.button('Predicción 3 meses', key=next(widget_id)):
                st.image("/workspaces/BiciMad_4geeks_ML/data/graficos/images/bikes3.png", 
                         caption='Predicción con valores absolutos sin límite computacional')
            if row1_col2.button('Predicción 6 meses', key=next(widget_id)):
                st.image("/workspaces/BiciMad_4geeks_ML/data/graficos/images/bikes6.png", 
                         caption='Predicción con valores absolutos sin límite computacional')
            if row1_col3.button('Predicción de 1 año', key=next(widget_id)):
                st.image("/workspaces/BiciMad_4geeks_ML/data/graficos/images/bikes12.png", 
                         caption='Predicción con valores absolutos sin límite computacional')

with col2:
# Crear un generador para las claves de los botones
    widget_id = (id for id in range(1,  10000))

    # Crear un menú desplegable con las opciones
    prediccion = st.selectbox(
        'Crea la experiencia:', 
        ['Minutos de viaje al mes', 'Distancia recorrida al mes', 'Bicicletas usadas cada mes']
    )