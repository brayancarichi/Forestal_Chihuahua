import streamlit as st
from ultralytics import YOLO
from ultralytics.solutions import object_counter


import imutils
import os
from os import mkdir
from datetime import date
from datetime import datetime
from getpass import getuser
import supervision as sv
from PIL import Image

import matplotlib.path as mplPath
import matplotlib.pyplot as plt



from PIL import Image

from ultralytics import YOLO
from ultralytics.solutions import object_counter


import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import imutils
import gdown

def deteccion(image):
    
    

    

   
    
    
    model = YOLO("pages/Models25/ArbolesChihuahua.pt")
    imagen = image
    result = model(imagen,imgsz = 640, conf = 0.1, show_labels=False,show_conf=False)[0]
    resultados = model.predict(imagen, imgsz = 640, conf = 0.1)
    detections = sv.Detections.from_ultralytics(result)
    alta = detections[detections.confidence > 0.1]
    
    leng = len(resultados)
    
    anotaciones = resultados[0].plot()
    haber = imutils.resize(anotaciones,width=640)
    
    
    haber = imutils.resize(anotaciones,width=1024)
    
    
    
    
    return haber



def deteccion2(image):
    
    model = YOLO("pages/Models25/ArbolesChihuahua.pt")
    imagen = image
    result = model(imagen,imgsz = 640, conf = 0.1, show_labels=False,show_conf=False)[0]
    resultados = model.predict(imagen, imgsz = 640, conf = 0.1)
    detections = sv.Detections.from_ultralytics(result)
    alta = detections[detections.confidence > 0.1]
    
    leng = len(resultados)
    
    anotaciones = resultados[0].plot()
    haber = imutils.resize(anotaciones,width=640)
    
    leng = len(alta)
    leng2 = str(leng)
    
    haber = imutils.resize(anotaciones,width=1024)
  
    
    
    return leng2


def main():
    
    st.header('Aplicación para el conteo de árboles en imágenes satelitales')
    st.success('A continuación, sube tu imagen en alguno de los formatos que aquí se mencionan y en un par de segundos obtendrás los arboles que se detectaron.   ')
    st.sidebar.image(".\Imagenes\CenGeo.jpeg")
    st.sidebar.info('Esta aplicación fue desarrollada mediante visión por computadora y redes neuronales convolucionales. Al ingresar la imagen al sistema esta detecta y contabiliza los arboles que detecta. Muy útil para hacer estimaciones de árboles dañados durante algún incendio.')
    st.sidebar.image('.\Imagenes\Arboles.png')
    file_uploader = st.file_uploader('Sube tu imagen en los siguientes formatos: ', type=['jpg', 'png'])

    if file_uploader is not None:
        image = Image.open(file_uploader)
        print(image)
        

        st.image(image)
        datos = deteccion(image)
        st.markdown('Los resultados de la imagen de salida fueron modificados con el fin de que sea más fácil para la red neuronal hacer las detecciones de los árboles')
        st.image(deteccion((image)))

        st.markdown(deteccion2((image)) + ' Árboles detectados')

        


if __name__ == "__main__":
    main()

