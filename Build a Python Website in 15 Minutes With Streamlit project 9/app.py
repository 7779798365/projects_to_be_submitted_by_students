import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="My Streamlit Website", page_icon="🌍", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Streamlit Website! 🚀")
    st.write(
        "This is a simple Python-based website built with **Streamlit**. "
        "You can create interactive and data-driven web apps in minutes!"
    )

    # User Input
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! 👋")

    # Interactive slider
    age = st.slider("Select your age:", 1, 100, 25)
    st.write(f"Your age is **{age}** years.")

    # Button Example
    if st.button("Click Me!"):
        st.balloons()

# About Page
elif page == "About":
    st.title("About This Website 📖")
    st.write(
        "This website is built using **Streamlit**, a powerful tool for creating web applications with Python. "
        "You can use it for data science, machine learning apps, and even full-fledged websites!"
    )

# Contact Page
elif page == "Contact":
    st.title("Contact Me 📩")
    st.write("If you have any questions, feel free to reach out!")

    # Contact Form
    email = st.text_input("Enter your email:")
    message = st.text_area("Enter your message:")
    
    if st.button("Send Message"):
        if email and message:
            st.success("📧 Your message has been sent!")
        else:
            st.error("Please fill in all fields.")