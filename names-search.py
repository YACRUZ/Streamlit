import streamlit as st
import pandas as pd

st.title("Search names")
DATA_URL = "dataset.csv"

@st.cache
def load_data_byname(name):
    data = pd.read_csv(DATA_URL) #read CSV
    filtered_data_byname = data[data["name"].str.contains(name)]
    return filtered_data_byname #return the dataframe

myname = st.text_input("nombre: ")
if(myname):
    filteredbyname = load_data_byname(myname) #call the function
    count_row = filteredbyname.shape[0]
    st.write(f"Total names : {count_row}")

    st.dataframe(filteredbyname)