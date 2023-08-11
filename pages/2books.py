import requests
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from PIL import Image


st.page_title=("Books | AcademEase")



st.title("Find books with ease using AcademEase!📚")
st.subheader("Searching the internet for books YOU need requires a lot of time- more than what you have to give. Here is a curated list made by students like you, just for you!")
st.sidebar.success("Where would you like to go?")
st.subheader("Physics Supplementary Reading")
df = pd.DataFrame(
    [
        {"Book Name": "Concepts of Physics by H.C. Verma", "Subject": "Physics"},
        {"Book Name": "Fundamentals of Physics by David Halliday, Robert Resnick, and Jearl Walker", "Subject": "Physics"},
        {"Book Name": "Physics for Scientists and Engineers by Paul A. Tipler", "Subject": "Physics"},
        {"Book Name": "The Feynman Lectures on Physics by Richard P. Feynman, Robert B. Leighton, and Matthew Sands", "Subject": "Physics"},
        {"Book Name": "Introduction to Classical Mechanics by David Morin", "Subject": "Physics"},
        {"Book Name": "Physics of the Impossible by Michio Kaku", "Subject": "Physics"},
        {"Book Name": "Storm in a Teacup by Helen Czerski", "Subject": "Physics"},
        {"Book Name": "On the Origin of Time by Thomas Hertog", "Subject": "Physics"},
        {"Book Name": "A Brief History of Time by Stephen Hawking", "Subject": "Physics"},
        {"Book Name": "Cosmos by Carl Sagan", "Subject": "Physics"},
        
    ]
)

st.dataframe(df, use_container_width=True)
st.subheader("Chemistry Supplementary Reading")
df1 = pd.DataFrame(
    [
        {"Book Name": "Chemistry: The Central Science by Theodore L. Brown, H. Eugene LeMay, and Bruce E. Bursten", "Subject": "Chemistry"},
        {"Book Name": "Principles of Chemical Nomenclature by GJ Leigh, HA Favre and WV Metanomski", "Subject": "Chemistry"},
        {"Book Name": "Chemistry: A Molecular Approach by Nivaldo J. Tro", "Subject": "Chemistry"},
        {"Book Name": "Chemistry: Concepts and Problems by Clifford C. Houk and Richard Post", "Subject": "Chemistry"},

    ]
)
st.dataframe(df1, use_container_width=True)
st.subheader("Biology Supplementary Reading")
df3 = pd.DataFrame(
    [
        {"Book Name": "How We Live and Why we Die by Lewis Wolper", "Subject": "Biology"},
        {"Book Name": "Emperor of Maladies by Siddhartha Mukherjee", "Subject": "Biology"},
        {"Book Name": "The Gene by Siddhartha Mukherjee", "Subject": "Biology"},
        {"Book Name": "Lehninger Principles of Biochemistry by David L. Nelson and Michael M. Cox", "Subject": "Biology"},
        {"Book Name": "Gene Machine by Venki Ramakrishnan", "Subject": "Biology"},
        {"Book Name": "Fundamentals of Biology, publisher: Wiley", "Subject": "Biology"},
        {"Book Name": "Campbell Biology", "Subject": "Biology"},
    ]
)
st.dataframe(df3, use_container_width=True)
st.divider()
st.subheader("Language and Literature")
df2 = pd.DataFrame(
     [
        {"Book Name": "Anna Karenina by Leo Tolstoy", "Subject": "English Literature"},
        {"Book Name": "The Picture of Dorian Gray by Oscar Wilde", "Subject": "English Literature"},
        {"Book Name": "To the Lighthouse by Virgina Woolf", "Subject": "English Literature"},
        {"Book Name": "East of Eden by John Steinbeck", "Subject": "English Literature"},
        {"Book Name": "Animal Farm by George Orwell", "Subject": "English Literature"},
        {"Book Name": "1984 by George Orwell", "Subject": "English Literature"},
        {"Book Name": "Anne of Green Gables by L.M. Montgomery", "Subject": "English Literature"},
        {"Book Name": "Middlemarch by George Eliot", "Subject": "English Literature"},
        {"Book Name": "The Brother's Karamazov by Fyodor Dostoevsky", "Subject": "English Literature"},
        {"Book Name": "Lord of the Flies by William Golding", "Subject": "English Literature"},
        {"Book Name": "The Great Gatsby by F.Scott Fitzgerald", "Subject": "English Literature"},
        {"Book Name": "Crime and Punishment by Fyodor Dostoevsky", "Subject": "English Literature"},
        {"Book Name": "The Castle by F.Kafka", "Subject": "English Literature"},
        {"Book Name": "Academic Journal: The American Prometheus by Kai Bird and Martin J. Sherwin", "Subject": "English Literature"},

    ]
)
st.dataframe(df2, use_container_width=True)

image5 = Image.open('dog.jpg')
st.text("")
st.text("")
st.text("")

st.image(image5, caption='Go study now!')
