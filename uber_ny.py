import pandas as pd
import numpy as np
import streamlit as st

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('uber_dataset.csv')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text('Loading data...')
data = load_data(100000)
data_load_state.text("Done! (using st.cache_resource)")

# Some number in the range 0-23
hour_to_filter = st.slider('day', 1, 30, 1)
filtered_data = data[data[DATE_COLUMN].dt.day == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
