import requests
import streamlit as st


st.set_page_config(
    page_title="Contact | AcademEase"
)
st.divider()



st.title("Contact Us!")
st.write("Have any suggestions? Please contact us!")
st.sidebar.success("Where would you like to go?")

def localcss(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

localcss("style/style.css"),

cform = """
<form action="https://formsubmit.co/ilinamukherjee2020@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Name: " required>
     <input type="email" name="email" placeholder="Email: " required>
     <textarea name="message" placeholder="Enter your message: " required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(cform, unsafe_allow_html=True)
with right_column:

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
