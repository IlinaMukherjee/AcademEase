import requests
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(
    page_title="Internships and Competitions| AcademEase"
)
st.sidebar.success("Where would you like to go?")


st.title("Internships and Competitions for High school students")
st.write("Participating in internships and competitions equips high school students with practical skills and real-world experiences that enhance their academic learning and future career prospects.")

st.write("At Academease, find the right internship for you!")
st.caption("If you're interested in adding more information to this list, feel free to contact us with suggestions!")

st.divider()

st.subheader("Internships: STEM oriented")
st.caption("At the moment we have only STEM internships but we will be adding more diversity in our categories in the future.")

st.markdown(
    """
    - Guided research programs [Indigo Research](https://www.indigoresearch.org/program/high-school#5)
    - Internship at NASA [STEMGateway](https://stemgateway.nasa.gov/public/s/explore-opportunities)
    - Summer School at Oxford with Oxford Associates [Oxford Royale](https://www.oxford-royale.com/)
    - [NASA for Student](https://www.nasa.gov/stem/forstudents/9-12/index.html)
    - AI Scholars [InspiritAI](https://www.inspiritai.com/)
    - The Summer Science Program [SSP](https://summerscience.org/)
    - [Research Science Institute](https://www.cee.org/programs/research-science-institute)
    - [Stanford Mathematics Camp](https://sumac.spcs.stanford.edu/sumac-about)
    - [MIT Programs](https://mitadmissions.org/apply/prepare/summer/)
    + More to be added!


"""
)

st.divider()
st.subheader("Competitions for High school students")

st.markdown("""

    **WRITING:**
    - The Queen's Commonwealth Essay Competition (QCEC)
    - International Elaine Hobson Literary Award 2022 
    - Immerse Essay Award Prize 2022
    - Harvard International Review Academic Writing Contest 
	 """
	 )

	
st.markdown("""
            **SCIENCE:**
            - Avogadro Exam
            - IRIS National Fair
            - [SARC Research Competition](https://www.researchcomp.org/prizes)
            - Breakthrough Junior Challenge
            - [World Science Scholars](https://worldsciencescholars.com/homepage/)
            """)
	
st.markdown("""
            **TECH:**
            - [ACSL](https://www.acsl.org/)
            - [ISEF](https://www.societyforscience.org/isef/)
            - [Technovation Girls](https://my.technovationchallenge.org/)
            """)
	
st.markdown("""
            **SOCIAL SERVICE:**
            - The Diana Awards
            - [RISE] (risefortheworld.org)
            For mentorship and guidance for your project,
            - [1m1b](https://activate1m1b.org/)
            """)
	
st.markdown("""
            **MATH:**
            - TOSC Techkriti
            - [Harvard MIT Math Competition](https://www.hmmt.org/)""")
	

st.write("""  + More to be added!
            
    """)

st.divider()
st.write("If you have any feedback or suggestions to improve AcademEase, head over to [our Contact Page](contact.py)")