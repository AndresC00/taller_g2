# prompt: antes instala streamlit 

!pip install streamlit plotly pandas seaborn matplotlib

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset de propinas
df = sns.load_dataset("tips")

# Configurar la app de Streamlit
st.title("Análisis de Propinas")
st.write("Este dashboard muestra análisis del dataset de propinas en un restaurante.")

# Seleccionar día de la semana
dias = df['day'].unique()
dia_seleccionado = st.selectbox("Selecciona un día:", dias)

df_dia = df[df['day'] == dia_seleccionado]

# Gráfico de relación entre total de la cuenta y propina
st.subheader(f"Relación entre total de cuenta y propina en {dia_seleccionado}")
fig, ax = plt.subplots()
sns.scatterplot(data=df_dia, x='total_bill', y='tip', hue='sex', ax=ax)
ax.set_xlabel("Total de la cuenta (USD)")
ax.set_ylabel("Propina (USD)")
st.pyplot(fig)

# Mostrar tabla de datos filtrados
st.subheader("Datos Filtrados")
st.dataframe(df_dia)
