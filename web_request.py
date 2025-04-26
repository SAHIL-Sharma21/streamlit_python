# web request in stremlit
import streamlit as st
import requests

st.title("Live currency convertor")
amout = st.number_input("Enter the amount in INR", min_value=1)

target_currency = st.selectbox("COnvert to: ", ["USD", "EUR", "GBP","JPY"])

if st.button("convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        converted = rate * amout
        st.success(f"{amout} INR = {converted: .2f} {target_currency}")
    else:
        st.error("Failed to fetch the conversion rate")