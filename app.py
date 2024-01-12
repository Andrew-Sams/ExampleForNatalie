import streamlit as st

st.set_page_config(
    page_title="Natalie's App",
    layout="wide",
)

st.title("Welcome to Natalie's App")

if st.button('Press Me'):
    st.text("Natalie")