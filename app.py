import streamlit as st

sf.setpage_config(
    page_title="Natalie's App",
    layout="wide",
)

st.write("# Welcome to Natalie's App")

if st.button('Press Me'):
    st.markdown("### Natalie!", safe=false)