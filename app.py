import openai
# from PIL import Image
import streamlit as st
from config import apikey

client = openai.Client(api_key=apikey)

def generate_image(image_discription, num_images):
    img_response = openai.images.generate(
        model="dall-e-3",
        prompt=image_discription, 
        size="1024x1024",
        quality="standard",
        n=1
    )
    
    image_url = img_response.data[0].url
    return image_url
st.set_page_config(page_title="HoriZon", page_icon="camera", layout="wide")

st.title("HoriZon Text to Image Generator")

st.subheader("Upload Your Prompt fot the Image.")
img_discription = st.text_input("Enter the image discription")
num_of_images = st.number_input("Number of images", min_value=1, max_value=10, value=1)

if st.button("Generate image ") :
    generate_image =generate_image(img_discription, num_of_images)
    st.image (image_url, caption="generate_image") # type: ignore

