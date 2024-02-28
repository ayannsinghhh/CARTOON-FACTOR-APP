### Cartoon Factor App
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AIzaSyCp4nTt730tybI_IiB7uVmwkm9WWtHXcnU")

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="Cartoon App")

st.header("Cartoon Factor App")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me the name of the cartoon with show name")

input_prompt="""
You are an expert in finding the cartoons from the images and telling the name of the cartoon along with the show
            

               1. Name - Name of the cartoon
               2. Show name - Name of the show
               3. Creater - Name of the maker
               4. Fun Fact - Interesting fact about the cartoon
               ----
               ----
"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)
