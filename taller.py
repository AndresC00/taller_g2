import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Cargar dataset de propinas
df = sns.load_dataset("tips")

# Configurar la app de Streamlit
st.title("Análisis de Propinas")
st.write("Este dashboard muestra análisis del dataset de propinas en un restaurante.")

# Selección de opciones para gráficos
tipo_grafico = st.selectbox("Selecciona un tipo de gráfico:", ["Histograma", "Scatter Plot", "Box Plot", "Violin Plot"])

if tipo_grafico == "Histograma":
    columna = st.selectbox("Selecciona una columna:", ["total_bill", "tip", "size"])
    fig, ax = plt.subplots()
    sns.histplot(df[columna], kde=True, ax=ax)
    st.pyplot(fig)

elif tipo_grafico == "Scatter Plot":
    x_col = st.selectbox("Selecciona la columna para el eje X:", ["total_bill", "tip", "size"])
    y_col = st.selectbox("Selecciona la columna para el eje Y:", ["total_bill", "tip", "size"])
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x_col, y=y_col, hue="sex", ax=ax)
    st.pyplot(fig)

elif tipo_grafico == "Box Plot":
    columna = st.selectbox("Selecciona una columna:", ["total_bill", "tip", "size"])
    fig, ax = plt.subplots()
    sns.boxplot(x="day", y=columna, data=df, ax=ax)
    st.pyplot(fig)

elif tipo_grafico == "Violin Plot":
    columna = st.selectbox("Selecciona una columna:", ["total_bill", "tip", "size"])
    fig, ax = plt.subplots()
    sns.violinplot(x="day", y=columna, data=df, ax=ax)
    st.pyplot(fig)
