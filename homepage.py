import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(
    page_title="Home | AcademEase"
)



st.title("AcademEase 📖")
st.sidebar.success("Where would you like to go?")


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_file = load_lottie_url("https://lottie.host/b620043c-0842-4546-8fe5-bf75fdbfeb53/kEO6r3egFH.json")


with st.container():
    st.subheader("Your one-stop website for everything school related!")
    st.write("Ever wanted to streamline your path to success? Look no further! Introducing our comprehensive website, your gateway to a world of opportunities. Get started on your journey to professional growth by exploring a diverse range of internships, thrilling competitions, and invaluable resources - all conveniently collated in one place. Unleash your potential today and pave the way for a brighter tomorrow with us!")
    st.write("##")
    st.divider()
    left_column, right_column = st.columns(2)
    with right_column:
        st_lottie(lottie_file, height=400, key="studyanime")
    with left_column:
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