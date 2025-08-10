import streamlit as st
from utils.layout import app_header

st.set_page_config(page_title="Economy • Markets • Portfolio", layout="wide")
app_header()
st.markdown(
    "Welcome! Use the left sidebar **Pages** to navigate:\n"
    "- **Global Economy** — world GDP map + macro indicators (World Bank)\n"
    "- **Markets** — indexes, yields (Yahoo Finance + FRED)\n"
    "- **Portfolio** — upload CSV, compare vs benchmark"
)