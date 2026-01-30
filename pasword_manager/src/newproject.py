import streamlit as st
import random
import pandas as pd
df = pd.DataFrame({'first column': [1, 2, 3, 4],
                   'second column ': [4, 7, 5, 8]})
df

q=st.slider('select a value',-50 , 50, step=10) 
st.write(q)
st.write('hello world!')
"""
    author: me
    date: today
"""

contact_type = st.selectbox(
    'what is your favorite color?',
    ('blue','yellow','pink')
)
contact_type = st.radio(
    'what is your favorite color?',
    ('blue','yellow','pink')
)
import numpy as np
if st.checkbox('show'):
    chart_data = pd.DataFrame(
       np.random.rand(20,3),
        columns= ['a','b','c'])
    st.line_chart(chart_data)

col1, col2, col3 = st.columns(3)
col1.write('1col')
col2.write('2col')
col3.checkbox('ssjhcsd')