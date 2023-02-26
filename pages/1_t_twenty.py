import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

file_dir = os.path.dirname(os.path.abspath(__file__))
p_dir = os.path.join(file_dir, os.pardir)
dir_of_interest = os.path.join(p_dir, "resources")

img_path = os.path.join(dir_of_interest, "images", "t20.jpg")
data_path = os.path.join(dir_of_interest, "data", "t20.csv")

st.header('Cricket t20')

img = image.imread(img_path)
st.image(img)

df = pd.read_csv(data_path)
st.dataframe(df)

Player = st.selectbox("Select the Player:", df['Player'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Player'] == Player], x="Mat")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Player'] == Player], y="Mat")
col2.plotly_chart(fig_2, use_container_width=True)