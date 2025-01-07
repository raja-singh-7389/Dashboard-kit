import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animation from a URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        st.error(f"Failed to load animation from {url}. Status code: {r.status_code}")
        return None
    return r.json()

# Open the image using Image.open() method
image = Image.open("Image.jpg")

# Page Configuration
st.set_page_config(layout="wide", page_title="Portfolio - Raja Singh Thakur")
st.title("My Portfolio Website")
st.divider()

# Add a Lottie animation to the About Section
st.subheader("Welcome")

# Load Lottie animation (use a URL from LottieFiles or your own)
lottie_url = "https://assets6.lottiefiles.com/packages/lf20_zdzyrxhx.json"  # Example Lottie URL
lottie_animation = load_lottie_url(lottie_url)

# Create two columns: one for the text and one for the image
col1, col2 = st.columns([2, 1])  # [2, 1] means the left column is 2x and right column is 1x

with col1:
    st.info("""
    **About Me**

    Hi! I’m Raja Singh Thakur. I am a passionate data scientist and analyst with a focus on turning data into actionable insights. With expertise in data visualization, statistical analysis, and machine learning, I enjoy solving complex problems and helping businesses make informed decisions. My goal is to uncover stories hidden within data and deliver clear, impactful solutions.
    """)

with col2:
    # Resize the image (width is set to 200px)
    st.image(image, caption="Raja Singh Thakur", use_container_width=False, width=200)

# Display the Lottie animation
if lottie_animation:
    st_lottie(lottie_animation, speed=1, width=400, height=400, key="animation1")

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
  Swami Vivekananda University, Sagar, Madhya Pradesh  
  Grade: 7.4 | Year: 2019-2024

- **School**:  
  XII - Shailesh Memorial School, Sagar, Madhya Pradesh | Grade: 7  
  X - Christ Convent School, Patna Bujurg, Rehli, Sagar, Madhya Pradesh
""")

# Navigation Menu
with st.container():
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
