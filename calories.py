# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai


os.getenv("GEMINI_API_KEY")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(image):
    input = """Reply only if image is related to food or not 
    if image is related give calories of the food and how it helps or affects to health and heart 
    else reply give me only food related image"""
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image])
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
# input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(image)
    st.subheader("The Response is")
    st.write(response)