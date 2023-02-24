import streamlit as st
from PIL import Image


st.title("My Curriculum Vitae")
image = Image.open('home/jeet-mac/streamlit/proj_2/resources/images/mypic.jpg')

st.image(image, caption='')
