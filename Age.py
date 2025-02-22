import streamlit as st
from datetime import datetime, date

st.title("Age Calculator")

st.write("Enter your Date of Birth:")

# User se Date of Birth input lo, default value 2000-01-01 set hai.
dob = st.date_input("Date of Birth", date(2000, 1, 1))

if dob:
    today = datetime.today().date()
    # Age calculate karne ka formula
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.write(f"Your age is: **{age}** years")
