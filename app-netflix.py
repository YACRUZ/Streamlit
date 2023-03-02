import streamlit as st 
import pandas as pd
import codecs

st.title('Netflix app')





@st.cache_data
def load_data(nrows):
    doc = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    return data   

data_load_state = st.text('Loading data...')
data = load_data(500)
data_load_state.text('Done ! (using st.cache)')

sidebar = st.sidebar
sidebar.image('img.jpeg')
sidebar.title('Yahir Jesus Jacome Cogco')
sidebar.title('S20006732')

agree = sidebar.checkbox("Mostrar todos los filmes")
if agree:
    st.header("Todos los filmes")
    st.dataframe(data)






@st.cache_data
def load_data_byname(name):
    doc = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc) #read CSV
    filtered_data_byname = data[data["name"].str.contains(name)]
    return filtered_data_byname

myname = sidebar.text_input("Titulo del filme: ")
if(myname):
    filteredbyname = load_data_byname(myname) #call the function
    count_row = filteredbyname.shape[0]
    st.write(f"Total filmes mostrados : {count_row}")


btfilm = sidebar.button('Buscar filmes')
if(btfilm):
    st.dataframe(filteredbyname)




#selected box
@st.cache_data
def load_data_bydir(direct):
    doc = codecs.open('movies.csv','rU','latin1')
    data = pd.read_csv(doc) #read CSV
    filtered_data_bydir = data[data['director'] == direct]

    return filtered_data_bydir

selected_sex =sidebar.selectbox('Seleccionar director ', data['director'].unique())
btndirector = sidebar.button('filtrar')

if(btndirector):
    filterbysex =load_data_bydir(selected_sex)
    count_row = filterbysex.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(filterbysex)


