import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # lendo os dados

st.header('Aplicativo de Anúncios de Carros')  # cabeçalho

hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")  # criar um histograma
    st.plotly_chart(fig, use_container_width=True)  # exibir um gráfico Plotly interativo

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:  # se o botão for clicado
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig2 = px.scatter(car_data, x="odometer", y="price")  # criar gráfico de dispersão
    st.plotly_chart(fig2, use_container_width=True)  # exibir gráfico