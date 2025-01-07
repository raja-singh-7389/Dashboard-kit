import streamlit as st  
from streamlit_option_menu import option_menu  

# Page Configuration  
st.set_page_config(layout="wide")  
st.title('My Portfolio Website')  
st.divider()  

# About Section  
st.subheader('Welcome')  
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

# Navigation Menu  
with st.container():  
    selected = option_menu(  
        menu_title=None,  # No title for the menu  
        options=["Contact", "Projects", "Blogs"],  
        icons=["chat-left-text-fill", "code-slash", "file-text-fill"],  # Add icons for all options  
        orientation="horizontal"  # Display menu horizontally  
    )  

# Dynamic Content  
if selected == "Contact":  
    st.subheader("Contact")  
    st.write("You can reach me at:")  
    st.write("- **Email**: raja1011singhrajput@gmail.com")  
    st.write("- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/your-profile)")  
    st.write("- **GitHub**: [Your GitHub](https://github.com/raja-singh-7389)")  

elif selected == "Projects":  
    st.subheader("Projects")  
    st.write("### Here are some of my recent projects:")  
    st.write("- **Penguin Species Prediction App**: A machine learning app to classify penguins based on physical attributes.")  
    st.write("- **Stock Price Prediction**: Time series analysis and forecasting of stock prices using ARIMA and LSTM.")  
    st.write("- **Customer Segmentation**: Cluster analysis for targeted marketing campaigns.")  

elif selected == "Blogs":  
    st.subheader("Blogs")  
    st.write("### Recent Blog Posts:")  
    st.write("- [Understanding Machine Learning Models](#)")  
    st.write("- [Data Visualization Best Practices](#)")  
    st.write("- [How to Start a Career in Data Science](#)")  
