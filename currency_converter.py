import streamlit as st

st.title("Currency Converter")

# User se amount input
amount = st.number_input("Enter amount to convert:", value=1.0, key="amount_input")

# Currency selection ke liye dropdown menus with unique keys
currencies = ("USD", "EUR", "INR", "PKR", "GBP")
from_currency = st.selectbox("From Currency", currencies, key="from_currency")
to_currency = st.selectbox("To Currency", currencies, key="to_currency")

# Conversion rates (example values)
conversion_rates = {
    "USD": 1.0,
    "EUR": 0.93,
    "INR": 82.0,
    "PKR": 280.0,
    "GBP": 0.81
}

# Convert button with unique key
if st.button("Convert", key="convert_button"):
    if from_currency in conversion_rates and to_currency in conversion_rates:
        # Pehle amount ko USD mein convert karo phir target currency mein
        amount_in_usd = amount / conversion_rates[from_currency]
        converted_amount = amount_in_usd * conversion_rates[to_currency]
        st.write(f"{amount} {from_currency} = **{converted_amount:.2f} {to_currency}**")
    else:
        st.write("Conversion rate not available.")
