import requests
import streamlit as st



st.page_title=("Discover | AcademEase")




with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Discover")
        st.write("In the wise words of ChatGPT,")
        st.caption("Embrace the day with a thirst for knowledge - seize the opportunity to learn something new and expand your horizons today. Every discovery is a step towards personal growth and a more enriched tomorrow.")
    with right_column:


st.sidebar.success("Where would you like to go?")



with st.container():
    left_column, right_column = st.columns(2)
    with right_column:
        st.subheader("Word of the Day")
        st.write(
            f'<iframe src="https://www.merriam-webster.com/word-of-the-day" width="320" height="800"></iframe>',
            unsafe_allow_html=True,
        )
    with left_column:
        st.subheader("Today's Wordle")
        st.write(
            f'<iframe src="https://www.nytimes.com/games/wordle/index.html" width="320" height="800"></iframe>',
            unsafe_allow_html=True,
        )

