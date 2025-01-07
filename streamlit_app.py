import streamlit as st
from streamlit_option_menu import option_menu

# Page Configuration
st.set_page_config(layout="wide", page_title="Portfolio - Raja Singh Thakur")
st.title("My Portfolio Website")
st.divider()

# Add GIF animations for "man waving hello" and "coder doing code"
# Replace these URLs with the actual links to your GIFs
man_waving_url = "https://media.giphy.com/media/3o6Zt2zADt92jvTyl6/giphy.gif"  # Example GIF URL for man waving
coder_gif_url = "https://media.giphy.com/media/2w0kS4jxpmkpW/giphy.gif"  # Example GIF URL for coder typing

# Display animation
st.subheader("Welcome")
st.write("Here are some animations:")

# Create two columns for the animations
col1, col2 = st.columns(2)

# Column 1: Man waving hello animation
with col1:
    st.image(man_waving_url, caption="Man Waving Hello", use_column_width=True)

# Column 2: Coder typing code animation
with col2:
    st.image(coder_gif_url, caption="Coder Typing Code", use_column_width=True)

# About Section
st.info("""
**About Me**

Hi! I’m Raja Singh Thakur. I am a passionate data scientist and analyst with a focus on turning data into actionable insights. With expertise in data visualization, statistical analysis, and machine learning, I enjoy solving complex problems and helping businesses make informed decisions. My goal is to uncover stories hidden within data and deliver clear, impactful solutions.
""")

# Certifications Section
st.write("""
### Certifications

- Advanced Probability Theory - IIT Delhi  
- Applied Linear Algebra in AI and ML - IIT Kharagpur  
- Data Analytics with Python - IIT Roorkee  
- Database Management System - IIT Kharagpur  
- Business Statistics - IIT Roorkee  
- Data Structures and Algorithms Using Python - Chennai Mathematical Institute  
- Enhancing Soft Skills and Personality - IIT Kanpur  

[View Certificates](https://github.com/raja-singh-7389/Portfolio-website.git)
""")
st.divider()

# Education Section
st.header("Education")
st.write("""
- **Graduation**:  
Bachleor in Computer Application
  Swami Vivekananda University, Sagar, Madhya Pradesh  
  Grade: 7.4 | Year: 2019-2024

- **School**:  
  XII - Shailesh Memorial School, Sagar, Madhya Pradesh | Grade: 7  
  X - Christ Convent School, Patna Bujurg, Rehli, Sagar, Madhya Pradesh
""")
st.divider()

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["Contact", "Projects", "Blogs"],
    icons=["chat-left-text-fill", "code-slash", "file-text-fill"],
    orientation="horizontal"
)

# Dynamic Content Rendering
if selected == "Contact":
    st.subheader("Contact")
    st.write("You can reach me at:")
    st.write("- **Email**: raja1011singhrajput@gmail.com")
    st.write("- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/raj-singh-8qoso)")
    st.write("- **GitHub**: [Your GitHub](https://github.com/raja-singh-7389)")

elif selected == "Projects":
    st.subheader("Projects")
    st.write("### Here are some of my recent projects:")
    st.write("- **Penguin Species Prediction App**: A machine learning app to classify penguins based on physical attributes.")
    st.write("[View App](https://penguin-species-prediction.streamlit.app)")
    st.write("- **Adidas Sales Dashboard**: A sales performance dashboard to visualize Adidas sales data.")
    st.write("[View Dashboard](https://adidas-sales-dashboard-121.streamlit.app)")

elif selected == "Blogs":
    st.subheader("Blogs")
    st.write("### Recent Blog Posts:")
    st.write("- **Understanding Machine Learning Models**")
    st.write("[View Blog](https://github.com/raja-singh-7389/Portfolio-website.git)")
    st.write("- **Data Visualization Best Practices**")
    st.write("[View Blog](https://github.com/raja-singh-7389/Portfolio-website.git)")
    st.write("- **How to Start a Career in Data Science**")
    st.write("[View Blog](https://github.com/raja-singh-7389/Portfolio-website.git)")
