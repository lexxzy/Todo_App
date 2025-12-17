import streamlit as st
from  PIL import Image

with st.sidebar:
    st.header("Image Uploader")
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
with st.expander("Camera Input"):
    camera_image = st.camera_input("camera")

if camera_image:
    Img = Image.open(camera_image)
    Img = Img.convert("L")
    st.image(Img)
