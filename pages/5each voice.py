import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="EachVoice | AcademEase"
)


st.sidebar.success("Where would you like to go?")

image5 = Image.open('eachvoice.png')

st.image(image5, caption='Coming soon...')

st.divider()