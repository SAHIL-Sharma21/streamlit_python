import streamlit as st

st.title("Hello from streamlit app")
st.subheader("Brewed with streamlit")
st.text("Welcome to streamlit application with python, and interactive app")

st.write("Choose your favourite game")


select_box = st.selectbox("Your favourite coffe: ", ["Cold Coffee", "Iced Latte", "Iced Americano"])
st.write(f'You choose {select_box} it was a excellent choice!')
st.success("you choice have been saved to the servers....")

st.write("Choose your favourite programming language")
programmin_language = st.selectbox("Your language", ["JavaScript", "Java", "Python", "C++", "C#", "Erlang"])
if programmin_language != "":
    st.write(f'you selected {programmin_language}, it is a great choice.')
    st.success("Yooohoooo!!!")