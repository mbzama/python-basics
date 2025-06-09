import streamlit as st

st.title("Streamlit Widgets Example")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", min_value=1, max_value=100, value=25)

if name:
    st.write(f"Hello, {name}, you are {age} years old!")

uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if uploaded_file is not None:
    content = uploaded_file.read()
    st.write("File content:")
    st.text(content.decode("utf-8"))