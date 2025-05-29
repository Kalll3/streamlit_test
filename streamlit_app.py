import streamlit as st
import requests

# -----------------------
# Title and Description
# -----------------------
st.title("🔥 Instagram Login (DEMO ONLY)")
st.write("This is a **fake login screen for demo/learning purposes only**. Your data is not stored or sent anywhere.")

# -----------------------
# Fake Login Form
# -----------------------
with st.form("login_form"):
    username = st.text_input("📱 Username")
    password = st.text_input("🔐 Password", type="password")
    submit = st.form_submit_button("Login")

if submit:
    st.success("✅ Login submitted (not actually logged in)")
    st.write("Here are the credentials you entered:")
    st.code(f"Username: {username}\nPassword: {password}", language='text')

# -----------------------
# Currency Converter
# -----------------------
st.header("💵 Currency Converter")

response = requests.get('https://api.vatcomply.com/rates?base=USD')
if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})
    currency_list = sorted(rates.keys())

    selected_currency = st.selectbox('Select a currency:', currency_list)
    amount_usd = st.number_input('Enter amount in USD:', min_value=0.0, value=1.0, step=0.1)

    rate = rates.get(selected_currency)
    converted_amount = amount_usd * rate

    st.success(f"{amount_usd} USD is equal to {converted_amount:,.2f} {selected_currency}")

    # Category
    if amount_usd >= 1_000_000_000:
        st.markdown("🚀 **You are a Billionaire!**")
    elif amount_usd >= 1_000_000:
        st.markdown("💸 **You are a Millionaire!**")
    else:
        st.markdown("🧢 Just a regular spender for now 😎")
else:
    st.error(f"API call failed with status code: {response.status_code}")

# -----------------------
# Joke Generator
# -----------------------
st.header("😂 Need a Laugh? Get a Random Joke!")

if st.button("Tell Me a Joke"):
    joke_response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if joke_response.status_code == 200:
        joke_data = joke_response.json()
        setup = joke_data.get("setup", "")
        punchline = joke_data.get("punchline", "")
        st.write("**" + setup + "**")
        st.write("*" + punchline + "*")
    else:
        st.error("Couldn't fetch a joke. Try again later!")
