import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng


st.title(":rainbow[Telecom X Latinoamérica: Análisis de Evasión de Clientes]", text_alignment='center')

st.subheader(":violet[**Descripción del proyecto**]", divider="rainbow")

proyecto = '''
El desafío **_Telecom X_** forma parte de la formación de Data Science del programa ONE, especificamente del curso Aprendiendo hacer ETL.

La empresa de telecomunicaciones **_Telecom X_** está enfrentando una alta tasa de cancelación y necesita comprender los factores que llevan a la pérdida de clientes.

El challenge consiste en recopilar, procesar y analizar los datos utilizando las bibliotecas Pandas, Matplotlib y Seaborn, con el objetivo de identificar los factores que están influyendo en la baja de clientes.

Para conocer qué razones están llevando a los clientes a darse de baja realizamos los siguientes pasos:
 1. Extraer los datos desde una API.
 2. Limpieza  y transformaciones de los datos.
 3. Análisis exploratorio de los datos. 
 4. Confección de un informe con los resultados y las recomendaciones para afrontar el problema de las cancelaciones.
'''
st.markdown(proyecto)

st.subheader(":violet[**Diccionario de datos**]")

col_1, col_2 = st.columns(2)

with col_1:
    x = st.slider('This is a slider', 1,10)
with col_2:
    st.write("El valor elegido de :red[***x***]", x)

st.subheader(":violet[**Vista previa**]")

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)

df = pd.DataFrame(
    {
        "col1": list(range(20)),
        "col2": rng(0).standard_normal(20),
        "col3": rng(1).standard_normal(20),
    }
)

st.area_chart(
    df,
    x="col1",
    y=["col2", "col3"],
    color=["#FF000080", "#0000FF80"],
)

with st.sidebar:
    st.title("Menú")
    st.header("Acerca del proyecto")
    st.write("This is my first app with STREAMLIT :)")
    st.header("Informe")
    st.header("ML Predicción")