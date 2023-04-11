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

# with tab2:
tab2.header("A dog")
tab2.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   with st.expander("testing"):
      st.header("tab 3 expanded")

with tab1:
   st.markdown("add to tabs later", unsafe_allow_html=True)


# you can have an expander under a tab but not a tab under an expander,
# unless you define the cols/tabs under the expander

with st.expander("COLUMNS EXPANDER"):
   col1, col2, col3 = st.columns(3)
   col1.markdown("foo c1")
   col1.markdown("lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=20)
   col2.markdown("bar c2")
   col3.markdown("foobar c3")

with st.expander("TABS EXPANDER"):
   tab4, tab5, tab6 = st.tabs(["t4", "t5", "t6"])
   tab4.header("head t4")
   tab5.header("head t5")
   tab6.header("head t6")
