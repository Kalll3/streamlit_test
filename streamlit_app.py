import streamlit as st 
import requests

# Set the app title 
st.title('My First Fvckinggg Apppp !!!') 

# Add a welcome message 
st.write('Welcome to my FKINGGGGGGGGGGAPPPPPPPPPPPPPPPPPPPPPPPP app!') 

# Custom message input
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
st.write('', widgetuser_input)

# API call for exchange rates
response = requests.get('https://api.vatcomply.com/rates?base=USD')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})

    # Select currency
    currency_list = sorted(rates.keys())
    selected_currency = st.selectbox('💱 Select the currency to convert to:', currency_list)

    # Input amount in USD
    amount_usd = st.number_input('💵 Enter amount in USD:', min_value=0.0, value=1.0, step=0.1)

    # Convert and display result
    rate = rates.get(selected_currency)
    converted_amount = amount_usd * rate
    st.success(f"{amount_usd} USD is equal to {converted_amount:,.2f} {selected_currency}")

    # Category output
    if amount_usd >= 1_000_000_000:
        st.markdown("🚀 **You are a Billionaire!**")
    elif amount_usd >= 1_000_000:
        st.markdown("💸 **You are a Millionaire!**")
    else:
