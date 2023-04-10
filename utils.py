"""Utility funcs for st app."""
import streamlit as st


def md_link(text: str, url: str):
    return f"[{text}]({url})"


def api_docs(anchor, URL="https://docs.streamlit.io/en/stable/api.html"):
    url = f"{URL}#{anchor}"
    text = f"docs - {anchor}"
    st.markdown("---")
    st.markdown(md_link(text, url))
