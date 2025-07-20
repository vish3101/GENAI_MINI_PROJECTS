from dotenv import load_dotenv

load_dotenv()

import os

import google.generativeai as genai
import streamlit as st
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model=genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(user_input, image_part, prompt):
    response = model.generate_content([
        {"text": prompt},
        image_part,
        {"text": user_input}
    ])
    return response.text



def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_part = {
            'mime_type': uploaded_file.type,
            'data': bytes_data
        }
        return image_part
    else:
        raise FileNotFoundError("No File Uploaded")

    
    
    
st.set_page_config(page_title='gemini invoive extractor')
st.header("Gemini Invoive Extractor")

input=st.text_input ("Input Pompt:",key='input')
uploaded_file=st.file_uploader("choose an image:",type=['jpeg','jpg','png'])

image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button("Tell me about the invoice")

input_prompt='''You are an expert in understanding inovices.The invoice may be written in any language. Translate internally if needed, but extract the relavant information as asked from the invoice
'''
if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input,image_data,input_prompt)
    st.subheader("The response is...")
    st.write(response)