"""Home page of multi-page streamlit app."""
import streamlit as st
import numpy as np
import pandas as pd
from utils import md_link, api_docs

# Add image as page favicon, rather than icon.
images_dir = "./images"
favicon_path = f"{images_dir}/favicon.ico"

st.set_page_config(
    page_title = "Hello World",
    # page_icon="🧊", # Use icon as page favicon.
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

cheatsheet_link = md_link(text="CHEATSHEET", url="https://docs.streamlit.io/library/cheatsheet")

st.markdown(f"# {cheatsheet_link} #")

# f"""
# <center>
# {st.image(f'{images_dir}/dark_tako_favicon.ico')}
# </center>
# """
st.image(f'{images_dir}/dark_tako_favicon.ico')

st.title("Computational Photography")

# st.write("## Multi-page Streamlit App 👋 ##")

# # st.markdown(f"<img src='{images_dir}/dark_tako_favicon.ico' alt='test alt text' style='width:128px;height:128px;'>", unsafe_allow_html=True)
# # st.components.v1.html(f"<img src='{images_dir}/zebra.jpg' alt='test alt text' style='width:128px;height:128px;'>")

# # # st.components.v1.html('<a href="default.asp"><img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;"></a>')
# # st.components.v1.html('<a href="default.asp"><img src="./images/favicon.png" alt="HTML tutorial" style="width:42px;height:42px;"></a>')
# # st.components.v1.html(f'<p><img src="{favicon_path}" alt="Smiley face" style="float:left;width:42px;height:42px;">The image will float to the left of the text.</p>')
# # st.components.v1.html('<p><img src="./images/favicon.ico.png" alt="Smiley face" style="float:left;width:42px;height:42px;">The image will float to the left of the text.</p>')
# # st.markdown("<p><img src='./images/favicon.ico.png' alt='Smiley face' style='float:left;width:42px;height:42px;'>The image will float to the left of the text.</p>", unsafe_allow_html=True)

# # st.sidebar.success("Select a demo above.")

# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )








# st.sidebar.title("This is sidebar")

# st.title("Let's try Streamlit")
# st.markdown(
#     "[Streamlit](https://www.streamlit.io/) is a great way to make a dashboard, "
#     "interactive or not."
# )

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Great features")
    st.markdown(
        """
    - you just write a python script that will render as webpage
    - there is a sleek HTML template, no extra formatting needed 
    - interactivity - you can get feedback from widgets and controls
    - native methods to draw charts, render latex, insert graphviz
    - dedicated hosting (in beta)
"""
    )

with col_b:
    st.subheader("You can see Streamlit as")
    st.markdown(
        """
- [Jupyter notebook](https://jupyter.org/) less code cells
- beefed-up [Handout][handout] (or Julia [Pluto.jl][pluto])
- [Flask][flask] without template setup
- Rstudio's [Shiny][shiny] in Python, with hosting
- another way to use [Plotly Dash](https://plotly.com/dash/) and [Bokeh](https://docs.bokeh.org/en/latest/index.html)
- the 'iPhone of Python'

[shiny]: https://shiny.rstudio.com/
[pluto]: https://github.com/fonsp/Pluto.jl
[handout]: https://github.com/danijar/handout    
[flask]: https://flask.palletsprojects.com/en/1.1.x/
    """
    )

# st.header("Minimal example")

# foo = """
# 1. Install: 
# ```
# $ pip install streamlit
# ```

# After installation ```streamlit``` will be available as a command line tool and as a package.

# 2. Make `my_app.py`:

# ```python
# import streamlit as st
# st.write("Hello, world!")
# ```

# 3. Run:

# ```
# $ streamlit run my_app.py
# ```

# 4. Point your broswer to http://localhost:8501. The page will refresh as you edit and save `my_app.py`.


# 5. Learn more with [tutorials](https://docs.streamlit.io/en/stable/getting_started.html).
# """
# foo

st.header("Small examples")

st.subheader("Input and display a number, show code")

with st.echo():
    x = st.number_input("A number please:")
    st.write("Just got", x)

st.subheader("Input and display a number, show code")

color = st.select_slider(
    "Select a color of the rainbow",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
)
st.write("My favorite color is", color)


st.subheader("Slider")

hour = st.slider("Hour", 0, 23, 12)

st.subheader("Display text, markdown, latex, variable, code")

st.write("<hr>")
st.text("Fixed width text")
st.markdown("_Markdown_")  # see *
st.latex(r"e^{i\pi} + 1 = 0")
st.write("Most objects")  # df, err, func, keras!
st.write(dict(a=1))
st.write(["st", "is <", 3])  # see *
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")

st.subheader("Line break")

st.markdown("---")

st.subheader("Graphviz chart")

st.graphviz_chart(
    """
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
"""
)

st.subheader("Checkbox as collapse control")

if st.checkbox("Show raw data"):
    st.subheader("Raw data")

st.subheader("Input text")

with st.echo():
    name = st.text_input("Name")
    st.text(name)

st.subheader("Show dataframe or table")
st.write(
    pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
)

st.subheader("Now there is a chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

st.subheader("Now there is a map")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.map(map_data)


st.header("Notes and discussion")

""" 
#### Limitations and feature requests

- cannot add raw html directly (safety concern)
- no obvious way to persist the result as html 
- table of contents (see below)

#### Mind model

- can persist data with  ```@st.cache()```
- show code via ```with st.echo():``` decorator
- multiple selection from list 

"""

