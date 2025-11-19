import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("data/vehicles_us.csv")

# Título / encabezado principal
st.title("Análisis de Vehículos en EE.UU. ")

# Encabezado para dataset
st.header("Exploración del Dataset")
st.subheader("Vista previa de los datos")
st.dataframe(df.head())

# Encabezado para gráficos
st.header("Visualización Interactiva")

# Botón para mostrar histograma
if st.button("Mostrar histograma de precios"):
    fig = px.histogram(df, x="price", nbins=50, title="Distribución de precios de vehículos")
    st.write("Histograma del campo `price`")
    st.plotly_chart(fig)

# Botón para gráfico de dispersión
if st.button("Mostrar gráfico de dispersión (Precio vs Kilometraje)"):
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        title="Relación entre Precio y Kilometraje",
        labels={"odometer": "Kilometraje", "price": "Precio (USD)"},
        opacity=0.6
    )
    st.write("Gráfico de dispersión: Precio vs Kilometraje")
    st.plotly_chart(fig_scatter)

