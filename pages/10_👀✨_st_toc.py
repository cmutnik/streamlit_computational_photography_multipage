import streamlit as st
# import numpy as np
# import pandas as pd
from utils import md_link, api_docs

st.set_page_config(
    page_title=" Demo App",
    page_icon="🧊",  # EP: how did they find a symbol?
    layout="wide",
    initial_sidebar_state="expanded",
)

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

st.markdown("## Insert Widgets ##", unsafe_allow_html=True)
st.components.v1.iframe("https://docs.streamlit.io/en/latest")
st.components.v1.iframe("http://localhost:8501/table_of_contents#table-of-contents",
                        width=None,
                        height=None,
                        scrolling=True)




st.title("Making TOC (experimental)")
st.markdown(
    """
Related links:

- https://discuss.streamlit.io/t/table-of-contents-widget/3470/8?u=epogrebnyak
- https://github.com/streamlit/streamlit/issues/726

"""
)


class Header:
    tag: str = ""

    def __init__(self, text: str):
        self.text = text

    @property
    def id(self):
        """Create an identifcator from text."""
        return "".join(filter(str.isalnum, self.text)).lower()

    @property
    def anchor(self):
        """Provide html text for anchored header. Example: 
           <h1 id="abcdef">Abc Def</h1>
        """
        return f"<{self.tag} id='{self.id}'>{self.text}</{self.tag}>"

    def toc_item(self) -> str:
        """Make markdown item for TOC listing. Example:
           '  - <a href='#abc'>Abc</a>'
        """
        return f"{self.spaces}- [{self.text}]('#{self.id}')"

    @property
    def spaces(self):
        return dict(h1="", h2=" " * 2, h3=" " * 4).get(self.tag)


assert Header("abc").spaces is None


class H1(Header):
    tag = "h1"


class H2(Header):
    tag = "h2"


assert H2("Abc").toc_item() == "  - [Abc]('#abc')"


class H3(Header):
    tag = "h3"


class TOC:
    """
    Original code, used with modifications:
    https://discuss.streamlit.io/t/table-of-contents-widget/3470/8?u=epogrebnyak
    """

    def __init__(self):
        self._headers = []
        self._placeholder = st.empty()

    def title(self, text):
        self._add(H1(text))

    def header(self, text):
        self._add(H2(text))

    def subheader(self, text):
        self._add(H3(text))

    def generate(self):
        text = "\n".join([h.toc_item() for h in self._headers])
        self._placeholder.markdown(text, unsafe_allow_html=True)

    def _add(self, header):
        st.markdown(header.anchor, unsafe_allow_html=True)
        self._headers.append(header)


class TOC_Sidebar(TOC):
    def __init__(self):
        self._headers = []
        self._placeholder = st.sidebar.empty()


def blah():
    for a in range(3):
        st.write("Blabla...")


toc = TOC()

toc.title("Title")

toc.header("Header 1")
blah()

toc.header("Header 2")
blah()

toc.subheader("Subheader 2.1")
blah()

toc.subheader("Subheader 2.2")
blah()

toc.generate()
