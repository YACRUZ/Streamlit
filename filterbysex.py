import streamlit as st
import pandas as pd

st.title("Streamlit - Filter by sex")
DATA_URL = "dataset.csv"

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL) #read CSV
    return data #return the dataframe

@st.cache_data
def load_data_bysex(sex):
    data = pd.read_csv(DATA_URL) #read CSV
    filtered_data_bysex = data[data['sex'] == sex]
    
    return filtered_data_bysex #return the dataframe

data = load_data ()
selected_sex = st.selectbox ('Select Sex', data['sex'].unique())
btnFilterbysex = st.button ('Filter by sex')

if (btnFilterbysex):
    filteredbysex = load_data_bysex(selected_sex) #call the function
    count_row = filteredbysex.shape[0]
    st.write(f"Total items : {count_row}")

    st.dataframe(filteredbysex)
    