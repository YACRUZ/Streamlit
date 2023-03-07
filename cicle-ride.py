import streamlit as st 
import pandas as pd
import numpy as np

st.title('Cicle Rides in NYC')

DATA_URL = ('citibike-tripdata.csv')
DATE_COLUMN = 'started_at'

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data  

data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text('Done! (using cache...)')


#Side

sidebar = st.sidebar
sidebar.image('img.jpeg')
sidebar.header('Yahir Jesus Jacome Cogco')
sidebar.header('S20006732')
sidebar.header('zs20006732@estudiantes.uv.mx')

agree = sidebar.checkbox("Show raw data")
if agree:
    st.header("Raw data")
    st.dataframe(data)

#Hist

if st.sidebar.checkbox('Recorridos por hora'):
    st.subheader('Numero de recorridos por hora')

    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)

#Map

hour_to_filter = st.sidebar.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Mapa de recorridos iniciados a las %s:00' % hour_to_filter)
st.map(filtered_data)
