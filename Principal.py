import streamlit as st

st.set_page_config(
    page_title='Forestal',
    layout="wide"
    
)
st.title('Plataforma para la detección y seguimiento de incendios forestales en el Estado de Chihuahua')
st.sidebar.success('select a page')

st.sidebar.image("Imagenes/CenGeo.jpeg")
st.sidebar.title("¿Quienes somos?")

markdown2 = "Somos una empresa 100% mexicana y nos dedicamos a ofrecer soluciones Geoespaciales en temas como agricultura de precisión, forestales, UMAS, etc."
st.sidebar.info(markdown2)

st.info("Los incendios forestales son unos de los desastres naturales que mayor impacto tienen en los ecosistemas ya que se pierde una cantidad enorme de vegetación. Los incendios forestales pueden suceder en cualquier momento, pero es en primavera y en verano donde existe un mayor riesgo de incendio y si a eso le sumamos que los fuertes vientos avivan significativamente el fuego pues el riesgo de propagación de los incendios es mayor.")
st.info("Es por eso por lo que tener plataformas espaciales que utilicen lo último en tecnología (imágenes satelitales, análisis de datos, Inteligencia Artificial) y que analicen todo en tiempo real es fundamental para monitorear nuestros bosques ya que lo que no se puede medir no se puede mejorar.")
st.info("Debido a esta necesidad y en apoyo de la conservación de ecosistemas en el Estado de Chihuahua, se desarrolló esta plataforma en la que se incluyen: detección de incendios en tiempo real, conteo de árboles mediante visión artificial y un semáforo forestal el cual indica que zonas hay mayor riesgo de incendios.")
st.image("Imagenes/Incendio2.jpeg",width=800)
st.text("Incendio de 16 de abril de 2025 visto desde la comunidad Álamo de Ojos Azules, Carichi, Chihuahua")



