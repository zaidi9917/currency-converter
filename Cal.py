import streamlit as st

st.title("Temperature Converter")

# User se temperature value input lo
temp = st.number_input("Enter Temperature Value:", value=0.0)

# Conversion ke options
conversion_option = st.selectbox("Select Conversion", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

if st.button("Convert"):
    if conversion_option == "Celsius to Fahrenheit":
        result = (temp * 9/5) + 32
        st.write(f"{temp} °C = **{result:.2f} °F**")
    else:
        result = (temp - 32) * 5/9
        st.write(f"{temp} °F = **{result:.2f} °C**")
