import streamlit as st
import streamlit.components.v1 as components


st.sidebar.image(".\Imagenes\CenGeo.jpeg")
st.sidebar.info('Esta plataforma fue desarrollada en Earth Engine y utiliza datos de la NASA para la detección de los puntos de calor. Dicha metodología se muestra en la siguiente imagen: ')
st.title('Plataforma para la detección de puntos de calor en tiempo real')
st.success('A continuación, se muestra la aplicación interactiva que detecta incendios en tiempo real. Puedes arrastrar el mapa, alejar o acercar el mapa, etc. Los puntos rojos, naranjas y amarillos corresponden con incendios forestales activos. Al presionar en algún punto, en la parte de debajo de la aplicación se mostrarán las coordenadas de ese punto especifico.')

components.iframe("https://ee-geoinfgeogee.projects.earthengine.app/view/incendioschihuahua", height=800)


st.sidebar.image(".\Imagenes\cirms.png")
st.sidebar.text('Fuente de la imagen: FIRMS FAQ NASA Earthdata')