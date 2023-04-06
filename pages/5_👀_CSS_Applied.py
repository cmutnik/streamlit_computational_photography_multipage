import streamlit as st
from PIL import Image

styles_dir = "./styles"
images_dir = "./images"
img_path = f"{images_dir}/dark_tako_favicon.ico.png"    

with open(f"{styles_dir}/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

image = Image.open(img_path)

st.markdown("image with `width=150`:")
st.image(image, width = 150)

st.markdown("image withouth `width` set")
st.image(image)

st.sidebar.success("Select a demo above.")
