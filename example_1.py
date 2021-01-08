import numpy as np
import pandas as pd
import streamlit as st

DATA_TIME = 'date/time'
DATA_URL = 'http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis='columns', inplace=True)
    data[DATA_TIME] = pd.to_datetime(data[DATA_TIME])
    return data


dados = load_data(100000)

st.title('Título do Painel')

hora = st.slider('escolha a hora', 0, 0, 23, 1)
dados = dados[dados[DATA_TIME].dt.hour == hora]

if st.checkbox('visualizar dados'):
    st.subheader('Dado Cru')
    st.write(dados)

st.subheader('Dado por Minuto em %sh' % hora)
st.bar_chart(np.histogram(dados[DATA_TIME].dt.minute, bins=60, range=(0, 60))[0])

st.subheader('Geo Dados em %sh' % hora)
st.map(dados)
