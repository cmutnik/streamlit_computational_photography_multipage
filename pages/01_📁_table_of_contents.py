"""Streamlit app for testing main page and table of contents."""
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ToC",
    page_icon="🧊",  # EP: how did they find a symbol?
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sample df to display in app.
df = pd.DataFrame(
    [[1, 2, 12, "why"], [3, 4, 34, "won't"], [5, 6, 56, "you"], [7, 8, 78, "die"]],
    columns=["A", "B", "AB", "quote"],
)

# Add a table of contents to the sidebar (hardcoded sections).
table_of_contents_for_sidebar = f"""
    # Table of Contents #
    1. [FOUO](#for-official-use-only)
        1. [Display dataframe](#display-dataframe)
        2. [Display table](#display-table)
    2. [Display json](#display-json)
        - [Display json](#display-json)
        - [Display metric](#display-metric)
    3. [Display TeX Math](#display-tex-math)
"""
st.sidebar.markdown(table_of_contents_for_sidebar, unsafe_allow_html=True)

table_of_contents_main_page = f"""
    # Table of Contents #
    1. [FOUO](#for-official-use-only)
        - [Display dataframe](#display-dataframe)
        - [Display table](#display-table)
    2. [Display json](#display-json)
    3. [Display metric](#display-metric)
    4. [Display TeX Math](#display-tex-math)
"""
st.markdown(table_of_contents_main_page, unsafe_allow_html=True)

# table_of_contents = f"""
# ## For Official Use Only
# ## Display dataframe
# ## Display table
# ## Display json
# ## Display metric
# ## Display TeX Math
# """
# st.markdown(table_of_contents, unsafe_allow_html=True)

st.title("SonTAU1")


st.markdown("[[_TOC_]]", unsafe_allow_html=True)
_html_ = r"[_TOC_]"
st.components.v1.html(_html_, width=None, height=None, scrolling=False)
st.markdown("[[TOC]]")
st.markdown("[[TOC]]", unsafe_allow_html=True)


# st.markdown("""
# ```mermaid
# graph TD;
#   A-->B;
#   A-->C;
#   B-->D;
#   C-->D;
# ```
# """, unsafe_allow_html=True)

st.markdown("A page for ya boi.")

# st.markdown(
#     f"""## For official use only ##
#     <font size=16>symbol</font> code""",
#     unsafe_allow_html=True,
# )

st.markdown(
    f"""## For Official Use Only ##
            <font size=16>symbol</font> code""",
    unsafe_allow_html=True,
)

st.markdown("### Display dataframe ###", unsafe_allow_html=True)
st.dataframe(df)

st.markdown("### Display table ###", unsafe_allow_html=True)
st.table(df.iloc[0:2])

st.markdown("### Display json ###", unsafe_allow_html=True)
st.json({"foo": "bar", "fu": "ba"})

st.markdown("### Display metric", unsafe_allow_html=True)
st.metric("My metric", 42, 2)
st.metric("My metric", 43, 3)

st.markdown("### Display TeX Math ###", unsafe_allow_html=True)
st.markdown("""
This math is inline: `$a^2+b^2=c^2$`.

This math is on a separate line using a `$$...$$` block:

$$
a^2+b^2=c^2
$$
""", unsafe_allow_html=True)



# import streamlit.components.v1 as components
# # embed streamlit docs in a streamlit app
# components.iframe("https://docs.streamlit.io/en/latest")
# st.components.v1.iframe("https://docs.streamlit.io/en/latest")
st.components.v1.iframe("#table-of-contents")


st.markdown("## Insert Widgets ##", unsafe_allow_html=True)
st.components.v1.iframe("https://docs.streamlit.io/en/latest")
st.components.v1.iframe("http://localhost:8501/table_of_contents#table-of-contents",
                        width=None,
                        height=None,
                        scrolling=True)


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


def blah(n_blahs=3):
    for a in range(n_blahs):
        st.write("Blabla...")


toc = TOC()

toc.title("Title")

toc.header("Header 1")
blah(n_blahs=2)

toc.header("Header 2")
blah(n_blahs=1)

toc.subheader("Subheader 2.1")
blah(n_blahs=1)

toc.subheader("Subheader 2.2")
blah()

toc.generate()
