#import streamlit as st
#uploaded_files = st.file_uploader('Choose a CSV file', accept_multiple_files=True)

#for uploaded_file in uploaded_files:
#    bytes_data = uploaded_file.read()
#    st.write('filename:', uploaded_file.name)
#    st.write(bytes_data)
    
    
import streamlit as st 
from PIL import Image
#from classify import predict

import requests
import urllib.request

st.title("Image Colorizer")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    #st.write(type(image))
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Save image
    image.save("image.png", format="png")
    
    file_name= 'image.png'
#    st.write(type(Image.open(uploaded_file)))

    # API request
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={
            'image': open(file_name, 'rb')
            #'image': image
        },
        headers={'api-key': '3c1099c1-224e-4875-8cd2-18a59c25421f'}
        )
    
    colorized_image = Image.open(requests.get(r.json()['output_url'], stream=True).raw)

    # Show image
    st.image(colorized_image, caption='Colorized Image.', use_column_width=True)