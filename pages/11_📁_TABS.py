"""Streamlit tab example."""
import streamlit as st

st.set_page_config(
    page_title = "tabs",
    page_icon="🧊",
)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
   st.markdown("add to original tab", unsafe_allow_html=True)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab1:
   st.markdown("add to tabs later", unsafe_allow_html=True)
