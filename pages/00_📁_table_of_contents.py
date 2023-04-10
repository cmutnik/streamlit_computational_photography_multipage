"""Streamlit app for testing main page and table of contents."""
import streamlit as st
import pandas as pd

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
