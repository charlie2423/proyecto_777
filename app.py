import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header('Análisis Exploratorio de Datos (EDA) de Vehículos')

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox para activar la opción de histograma
build_histogram = st.checkbox('Mostrar opciones de visualización')

if build_histogram:
    st.write('Opciones para visualizar los datos del odómetro')

    # Botón para histograma
    if st.button('Construir histograma'):
        st.write('Creación de un histograma para la columna "odometer"')
        fig_hist = px.histogram(car_data, x="odometer")
        st.plotly_chart(fig_hist, use_container_width=True)

    # Botón para gráfico de dispersión
    if st.button('Construir gráfico de dispersión (odómetro vs precio)'):
        st.write('Creación de un gráfico de dispersión: odómetro vs precio')
        fig_scatter = px.scatter(car_data, x="odometer", y="price")
        st.plotly_chart(fig_scatter, use_container_width=True)
