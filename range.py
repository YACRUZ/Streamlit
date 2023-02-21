import streamlit as st
import pandas as pd

st.title("Streamlit - Search range")
DATA_URL = "https://firebasestorage.googleapis.com/v0/b/streamlit-5b976.appspot.com/o/YACRUZ%2Fcsv%2Fdataset.csv?alt=media&token=87eee1e4-db35-4320-8fb1-955873cf8d88"

@st.cache_data
def load_data_byrange(startid, endid):
    data = pd.read_csv(DATA_URL) #read CSV
    filtered_data_byrange = data[(data['index'] >= startid) & (data['index'] <= endid)]
    
    return filtered_data_byrange #return the dataframe

startid = st.text_input ('Start index: ')
endid = st.text_input ('End index: ')
btnRange = st.button ('Search by range')

if (btnRange):
    filteredbyrange = load_data_byrange(int (startid), int (endid)) #call the function
    count_row = filteredbyrange.shape[0]
    st.write(f"Total items : {count_row}")

    st.dataframe(filteredbyrange)