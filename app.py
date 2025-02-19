import streamlit as st

# Set the page title
st.title("Siddeeeq's Web App")

# Add some text
st.write("Welcome to my web app!")

# User input
name = st.text_input("Enter your name:")

# Display dynamic output
if name:
    st.success(f"Hello, {name}! Glad to have you here.")

if name.lower() == "falamata" or name.lower() == "ameerah":
    st.write(f"I LOVE YOU SO MUCH MY DEAR {name.upper()}!")
    st.write(f"How is Egypt?")
    st.write("")
    st.write(f"Stay Safe!")
