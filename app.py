import streamlit as st
from streamlit_extras.app_logo import add_logo
from PIL import Image

# add kitten logo
# icon = Image.open('') --> page_icon=icon

st.set_page_config(page_title="Caso BiciMad, evolución del negocio | By Rubén Carrasco & Juan Lizondo",
                   page_icon="🧊",
                   layout="wide",
                   initial_sidebar_state="expanded"
 )          

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
    # Botones y imágenes basados en la opción seleccionada
    if prediccion == 'Minutos de viaje al mes':
        if st.button('Predicción de 3 meses', key=next(widget_id),):
            st.image("C:/Users/LuyinPC/Desktop/Bici-Mad/images_ppt/minutes3.png")
        if st.button('Predicción de 6 meses', key=next(widget_id)):
            st.image("https://github.com/Proyect-Final-4Geeks-RJ/BiciMad_4geeks_ML/blob/main/data/graficos/images/minutes6.png")
        if st.button('Predicción de 1 año', key=next(widget_id)):
            st.image("https://github.com/Proyect-Final-4Geeks-RJ/BiciMad_4geeks_ML/blob/main/data/graficos/images/minutes12.png")

    elif prediccion == 'Distancia recorrida al mes':
        if st.button('Predicción de 3 meses', key=next(widget_id)):
            st.image("https://github.com/Proyect-Final-4Geeks-RJ/BiciMad_4geeks_ML/blob/main/data/graficos/images/distance3.png")
        if st.button('Predicción de 6 meses', key=next(widget_id)):
            st.image("https://github.com/Proyect-Final-4Geeks-RJ/BiciMad_4geeks_ML/blob/main/data/graficos/images/distance6.png")
        if st.button('Predicción de 1 año', key=next(widget_id)):
            st.image("https://github.com/Proyect-Final-4Geeks-RJ/BiciMad_4geeks_ML/blob/main/data/graficos/images/distance12.png")

    elif prediccion == 'Bicicletas usadas cada mes':
        if st.button('Predicción de 3 meses', key=next(widget_id)):
            st.image("https://github.com/Proyect-Final-4Geeks-RJ/BiciMad_4geeks_ML/blob/main/data/graficos/images/bikes3.png")
        if st.button('Predicción de 6 meses', key=next(widget_id)):
            st.image("https://github.com/Proyect-Final-4Geeks-RJ/BiciMad_4geeks_ML/blob/main/data/graficos/images/bikes6.png")
        if st.button('Predicción de 1 año', key=next(widget_id)):
            st.image("https://github.com/Proyect-Final-4Geeks-RJ/BiciMad_4geeks_ML/blob/main/data/graficos/images/bikes12.png")

