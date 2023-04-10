import streamlit as st

images_dir = "./images"
favicon_path = f"{images_dir}/favicon.ico"

col1, col2, col3 = st.columns([2,4,2])

with col1:
    st.write("#### test col1 ####")
    st.markdown("`col1` was **Successful**")

with col2:
    st.image(favicon_path)

with col3:
    st.markdown("This is `col3`")
    st.text("Some other text")
    st.image(f"{images_dir}/dark_tako_favicon.ico")
