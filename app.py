import streamlit as st

# Set the page title
st.title("My First Streamlit Web App")

# Add some text
st.write("Welcome to my first Streamlit app!")

# User input
name = st.text_input("Enter your name:")

# Display dynamic output
if name:
    st.success(f"Hello, {name}! Glad to have you here.")
