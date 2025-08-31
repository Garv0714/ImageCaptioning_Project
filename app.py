import streamlit as st
from inference import generate_caption

st.title("🖼️ Image Captioning Demo")
uploaded_file = st.file_uploader("Upload an image")

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())
    st.image("temp.jpg")
    caption = generate_caption("temp.jpg")
    st.write("**Generated Caption:**", caption)