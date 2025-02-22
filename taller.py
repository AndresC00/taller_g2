import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

# URL del conjunto de datos en formato CSV
url = "https://www.datos.gov.co/resource/y628-5q9a.csv"

# Cargar los datos en un DataFrame
df = pd.read_csv(url)

# Filtrar las columnas relevantes
df = df[['condicion_victima']].dropna() # Select only one 'condicion_victima' column

# Count the occurrences of each victim condition
condition_counts = df['condicion_victima'].value_counts()

# Create a bar chart using Plotly Express
fig = px.bar(
    x=condition_counts.index, 
    y=condition_counts.values,
    labels={'x': 'Condición de la Víctima', 'y': 'Cantidad de Casos'},
    title='Condición de la Víctima'
)
st.plotly_chart(fig)
