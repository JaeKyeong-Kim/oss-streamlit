import streamlit as st



x = st.slider('Select a value')
st.write(x, 'is a square ', x * x)

st.title('App title')
st.header('header - Markdown')
st.markdown('markdown - Header')
st.subheader('subheader')
st.caption('caption')
st.code('x=2021')
st.latex(r'''a+ar^1+ar^2+ar^3''')

