import streamlit as st 
import requests

# Set the app title 
st.title('My First Fvckinggg Apppp !!!') 

# Add a welcome message 
st.write('Welcome to my FKINGGGGGGGGGGAPPPPPPPPPPPPPPPPPPPPPPPP app!') 

# Create a text input for message
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
st.write('', widgetuser_input)

# API call to get exchange rates
response = requests.get('https://api.vatcomply.com/rates?base=USD')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})

    # Currency selection
    currency_list = sorted(rates.keys())
    selected_currency = st.selectbox('💱 Select the currency to convert to:', currency_list)

    # Amount input
    amount_usd = st.number_input('💵 Enter amount in USD:', min_value=0.0, value=1.0, step=0.1)

    # Perform conversion
    rate = rates.get(selected_currency)
    converted_amount = amount_usd * rate

    # Display result
    st.success(f"{amount_usd} USD is equal to {converted_amount:.2f} {selected_currency}")
else:
    st.error(f"API call failed with status code: {response.status_code}")
