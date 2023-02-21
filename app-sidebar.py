# Importamos la librería Streamlit
import streamlit as st

# Crear el título para la aplicación web
st.title("App con Sidebar")

# Creamos el sidebar
sidebar = st.sidebar

# Agregamos un titulo y texto al sidebar
sidebar.title("Esta es el sidebar")
sidebar.write("Datos del sidebar")

st.header("Header 1")
st.header("Header 2")
st.write("Datos del content")