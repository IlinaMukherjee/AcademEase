import requests
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home | AcademEase"
)



st.title("AcademEase 📖")
st.sidebar.success("Where would you like to go?")




with st.container():
    st.subheader("Your one-stop website for everything school related!")
    st.write("Ever wanted to streamline your path to success? Look no further! Introducing our comprehensive website, your gateway to a world of opportunities. Get started on your journey to professional growth by exploring a diverse range of internships, thrilling competitions, and invaluable resources - all conveniently collated in one place. Unleash your potential today and pave the way for a brighter tomorrow with us!")
    st.write("##")
    st.divider()

    st.subheader("From internships to resources, we have it all!")
    st.write("##")
    st.write(
         """
        - Find opportunities in all fields!
        - Information on competitions, regional, national and international
        - Resources— extra reading, books and other free materials!
         - Write in our student-run magazine!
         """
        )


st.divider()
image = Image.open('Bosons.png')

st.image(image, caption='100% AcademEase recommended motivation')

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.caption("Animation credits: LottieFiles")
