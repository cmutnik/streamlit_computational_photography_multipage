"""Home page of multi-page streamlit app."""
import streamlit as st

# Add image as page favicon, rather than icon.
images_dir = "./images"
favicon_path = f"{images_dir}/favicon.ico"


st.set_page_config(
    page_title = "Hello World",
    # page_icon="👋", # Use icon as page favicon.
    page_icon = favicon_path, # Add image as page favicon, rather than icon.
    layout = "wide",
    initial_sidebar_state = "auto"
    # initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

st.image(f'{images_dir}/dark_tako_favicon.ico')

st.title("Computational Photography")

st.write("## Multi-page Streamlit App 👋 ##")

# st.markdown(f"<img src='{images_dir}/dark_tako_favicon.ico' alt='test alt text' style='width:128px;height:128px;'>", unsafe_allow_html=True)
# st.components.v1.html(f"<img src='{images_dir}/zebra.jpg' alt='test alt text' style='width:128px;height:128px;'>")

# # st.components.v1.html('<a href="default.asp"><img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;"></a>')
# st.components.v1.html('<a href="default.asp"><img src="./images/favicon.png" alt="HTML tutorial" style="width:42px;height:42px;"></a>')
# st.components.v1.html(f'<p><img src="{favicon_path}" alt="Smiley face" style="float:left;width:42px;height:42px;">The image will float to the left of the text.</p>')
# st.components.v1.html('<p><img src="./images/favicon.ico.png" alt="Smiley face" style="float:left;width:42px;height:42px;">The image will float to the left of the text.</p>')
# st.markdown("<p><img src='./images/favicon.ico.png' alt='Smiley face' style='float:left;width:42px;height:42px;'>The image will float to the left of the text.</p>", unsafe_allow_html=True)

# st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
