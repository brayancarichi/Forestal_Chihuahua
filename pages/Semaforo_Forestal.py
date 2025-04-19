import streamlit as st
import streamlit.components.v1 as components
st.title('Semáforo forestal estatal')

st.sidebar.image(".\Imagenes\CenGeo.jpeg")
st.sidebar.info('El semáforo forestal es una plataforma web interactiva que utiliza Machine Learning y evaluación multicriterio para determinar que zonas cuentan con riesgo de incendio. Para esta evaluación se utilizan variables como la humedad relativa, temperatura, velocidad del viento, una capa de restricciones y los usos del suelo.')

st.success('Puedes interactuar libremente con la aplicación interactiva. Color verde significa que no hay riesgo de incendio. Amarillo que hay un riesgo medio de incendios y tonalidades rojas significa que hay mucho riesgo de incendio.')

components.iframe("https://ee-geoinfgeogee.projects.earthengine.app/view/semaforo-forestal-chihuahua", height=800)