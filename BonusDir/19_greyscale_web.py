import streamlit as st
from PIL import Image

st.subheader("Colour to greyscale image converter")

with st.expander("Start Camera"):
    # Allows user to take a 'selfie' photo
    camera_image = st.camera_input("Camera")
if camera_image != None:
    # Create a PIL (pillow) var of the image & convert the image to grayscale
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    #display the image
    st.image(gray_img)

with st.expander("Upload Image"):
    uploaded_image = st.file_uploader("Upload Image")
if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)




