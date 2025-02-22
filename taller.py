import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset público
df = pd.read_csv("https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv")

# Filtrar datos recientes
df = df[df['Year'] >= 2000]

# Configurar la app de Streamlit
st.title("Visualización de Datos Económicos")
st.write("Este dashboard muestra la evolución del PIB de diferentes países desde el año 2000.")

# Seleccionar país
paises = df['Country Name'].unique()
pais_seleccionado = st.selectbox("Selecciona un país:", paises)

df_pais = df[df['Country Name'] == pais_seleccionado]

# Gráfico de evolución del PIB
st.subheader(f"Evolución del PIB en {pais_seleccionado}")
fig, ax = plt.subplots()
sns.lineplot(data=df_pais, x='Year', y='Value', ax=ax)
ax.set_ylabel("PIB en USD")
st.pyplot(fig)

# Mostrar tabla de datos
st.subheader("Datos del PIB")
st.dataframe(df_pais)
