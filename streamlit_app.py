import streamlit as st 
import requests

# Set the app title 
st.title('My First Fvckinggg Apppp !!!') 

# Add a welcome message 
st.write('Welcome to my FKINGGGGGGGGGGAPPPPPPPPPPPPPPPPPPPPPPPP app!') 

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 

# Display the customized message 
st.write('', widgetuser_input)

# API call to get exchange rates
response = requests.get('https://api.vatcomply.com/rates?base=USD')

if response.status_code == 200:
    data = response.json()
    rates = data.get('rates', {})

    # Currency selection box
    currency_list = sorted(rates.keys())  # Sort for better UX
    selected_currency = st.selectbox('Select the currency you want to see:', currency_list)

    # Show selected currency rate
    selected_rate = rates.get(selected_currency)
    if selected_rate:
        st.write(f"💱 Exchange rate for USD to {selected_currency}: **{selected_rate}**")
    else:
        st.warning(f"Currency {selected_currency} not found.")
else:
    st.error(f"API call failed with status code: {response.status_code}")
