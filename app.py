from openai import OpenAI
from PIL import Image
import streamlit as st
from config import apikey


st.set_page_config(page_title="HoriZon Image to Text", page_icon="camera", layout="wide")

st.title("OpenAI Image to Text")

st.subheader("Upload an image and get the text from it.")
img_discription = st.text_input("Enter the image discription")
num_of_images = st.number_input("Number of images", min_value=1, max_value=10, value=1)

if st.button("Generate image ") :
    pass
