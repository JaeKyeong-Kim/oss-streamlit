import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


x = st.slider('Select a value')
st.write(x, 'is a square ', x * x)

st.title('App title')
st.header('header - Markdown')
st.markdown('markdown - Header')
st.subheader('subheader')
st.caption('caption')
st.code('x=2021')
st.latex(r'''a+ar^1+ar^2+ar^3''')

rand=np.random.normal(1,2,size=20)
fig, ax= plt.subplots0
ax.hist(rand, bins=15)
st.pyplot(fig)

