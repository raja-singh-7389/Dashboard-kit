import streamlit as st
from stream_option_menu import option_menu

st.set_page_config(layout="wide")
st.title('My Portfolio website')
st.divider()

st.subheader('Welcome')

st.info("""
About Me

Hi! I’m Raja Singh Thakur, I am a passionate data scientist and analyst with a focus on turning data into actionable insights. With expertise in data visualization, statistical analysis, and machine learning, I enjoy solving complex problems and helping businesses make informed decisions. My goal is to uncover stories hidden within data and deliver clear, impactful solutions.
       """)

st.write('''Certifications

- Advance probability theory - IIT Delhi
- Applied Linear Algebra in AI and ML - IIT Kharagpur
- Data Analytics with Python - IIT Roorkee
- Database Management System - IIT Kharagpur
- Business Statistics - IIT Roorkee
- Data structures And Algorithms using Python - Chennai Mathematical Institute
- Enhacing soft skills and Personlity - IIT Kanpur

''')
st.write("[View certificate](https://github.com/raja-singh-7389/Portfolio-website.git)")

st.divider()

with st.container():
    selected = option_menu(
        menu_title=None,  # No title for the menu
        options=["Contact", "Projects", "Blogs"],
        icons=["chat-left-text-fill", "code-slash", "file-text-fill"],  # Add icons for all options
        orientation="horizontal"  # Display menu horizontally
    )


if selected == "Contact":
    st.write("You selected **Contact**.")
elif selected == "Projects":
    st.write("You selected **Projects**.")
elif selected == "Blogs":
    st.write("You selected **Blogs**.")
