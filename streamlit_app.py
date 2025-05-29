import streamlit as st 
import requests
import pyfiglet

# Set the app title 
st.title('My First Fvckinggg Apppp !!!') 

# Add a welcome message 
st.write('Welcome to my FKINGGGGGGGGGGAPPPPPPPPPPPPPPPPPPPPPPPP app!') 

# Create a text input 
widgetuser_input = st.text_input('Enter a custom message to turn into ASCII art:', 'Hello, Streamlit!') 

# Generate ASCII art using pyfiglet
ascii_art = pyfiglet.figlet_format(widgetuser_input)

# Display the ASCII art inside a code block
st.code(ascii_art, language='text')

# Add a button to copy ASCII art
st.download_button('Copy ASCII Art', ascii_art, file_name='ascii_art.txt')

# API calls
response = requests.get('https://api.vatcomply.com/rates?base=USD')

if response.status_code == 200:
    data = response.json()
    st.write('Exchange Rates Output:')
    st.json(data)  # nicely formatted JSON output
else:
    st.error(f"API call failed with status code: {response.status_code}")
