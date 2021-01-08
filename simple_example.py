import pandas as pd
import streamlit as st

st.title('Hi World')

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

with st.echo():
    x = 10

with st.echo():
    y = 42

with st.echo():
    z = x + y
    st.write(z)