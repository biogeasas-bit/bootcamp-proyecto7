# bootcamp-proyecto7
# Proyecto: Análisis de Vehículos Usados 🚗📊

Esta aplicación web fue creada como parte del bootcamp de análisis de datos.  
Permite explorar un conjunto de datos con información de vehículos usados publicados en Estados Unidos.

## Descripción del proyecto

La aplicación está construida con **Streamlit** y permite al usuario interactuar con los datos de manera sencilla, generando visualizaciones básicas para entender mejor los precios y características de los vehículos.

##  Funcionalidad de la aplicación

La aplicación ofrece:

- Visualización de las primeras filas del dataset
- Un botón que genera un **histograma** del precio de los vehículos
- Otro botón que genera un **gráfico de dispersión** (precio vs kilometraje)
- Gráficos generados con Plotly Express

## Tecnologías utilizadas

- Python  
- Streamlit  
- Pandas  
- Plotly Express  

## ▶️ Cómo ejecutar la aplicación

1. Activa el entorno virtual del proyecto  
2. Instala dependencias:

```bash
pip install -r requirements.txt
streamlit run app.py
