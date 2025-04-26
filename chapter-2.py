import streamlit as st

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Your chai is being brewed!")

add_masala = st.checkbox("Add tea leaves")
if add_masala:
    st.write("tea leaves added to you chai")

tea_type = st.radio("Pick you chai base: ", ["Milk", "sugar", "water", "Almond Milk"])
st.write(f'slected {tea_type} for the option')

flavor = st.selectbox("Choose flavour", ["Adrak", "Lemon", "kesar", "Tulsi"])
st.write(f'Selected flavour {flavor}')

sugar  = st.slider("sugar level", 0, 5, 3)

# uncontrolled input 
cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)
st.write(f"Selected sugar level {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Ther cutomer name is {name}")

dob = st.date_input("Select yourr dateof birth")
st.write(f'you date of birth is {dob}')