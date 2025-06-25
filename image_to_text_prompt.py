import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

GOOGLE_API_KEY=load_dotenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model=genai.GenerativeModel('gemini-1.5-flash')

def get_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
        
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")

st.header('Gemini Application')
input=st.text_input("Input Prompts, ",key='input')

uploaded_file=st.file_uploader("choose an image, ",type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_container_width=True)

submit=st.button("Tell me about this image")

if submit:
    response=get_response(input,image)
    st.subheader("The response is...")
    st.write(response)


