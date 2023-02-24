import streamlit as st
from PIL import Image


st.title("My Curriculum Vitae")
image = Image.open('mypic.jpg')

st.image(image, caption='')
