import streamlit as st
import requests

# Title
st.title("🔥 Instagram Login (DEMO ONLY)")

st.write("This is a **fake login screen for demo/learning purposes only**. Your data is not stored or sent anywhere.")

# Fake login form
with st.form("login_form"):
    username = st.text_input("📱 Username")
    password = st.text_input("🔐 Password", type="password")
    submit = st.form_submit_button("Login")

# After clicking login
if submit:
    st.success("✅ Login submitted (not actually logged in)")
    st.write("Here are the credentials you entered:")
    st.code(f"Username: {username}\nPassword: {password}", language='text')

# Optional: Show exchange rates just like before
response = requests.get('https://api.vatcomply.com/rates?base=USD')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})
    currency_list = sorted(rates.keys())
    selected_currency = st.selectbox('💱 Select a currency to view rate from USD:', currency_list)
    rate = rates.get(selected_currency)
    st.info(f"USD to {selected_currency}: {rate}")
else:
    st.error(f"Failed to fetch exchange rates: {response.status_code}")
