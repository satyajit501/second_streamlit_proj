import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
file_directory = os.path.dirname(os.path.abspath(__file__))

# absolute path to this file's root directory
parent_directory = os.path.join(file_directory, os.pardir)

# absolute path of directory of interest
dir_of_interest = os.path.join(parent_directory,"resources")

image_path = os.path.join(dir_of_interest, "images", "iris.jpg")
data_path = os.path.join(dir_of_interest, "data", "iris.csv")


st.title("Dashboard - Iris Data")

img = image.imread(image_path)
st.image(img)

df = pd.read_csv(data_path)
st.dataframe(df)

species = st.selectbox("Select the species:",df["Species"].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Species'] == species], x="SepalLength")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Species'] == species], y="SepalLength")
col2.plotly_chart(fig_2, use_container_width=True)
