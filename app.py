import pandas as pd
import plotly.express as px
import streamlit as st

# Título do aplicativo
st.header("Dashboard de Anúncios de Veículos")

# Carregar os dados
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar uma amostra dos dados
st.write("Visualização inicial dos dados")
st.dataframe(car_data.head())

# Histograma
hist_button = st.button('Criar Histograma')

if hist_button:
    st.write('Distribuição da quilometragem dos veículos')

    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribuição da Quilometragem'
    )

    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersão
scatter_button = st.button('Criar Gráfico de Dispersão')

if scatter_button:
    st.write('Relação entre preço e quilometragem')

    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Preço x Quilometragem'
    )

    st.plotly_chart(fig, use_container_width=True)