import streamlit as st
from datetime import date
st.title("Hello! This is age calculator")
current_Date=date.today()
selected_Date=st.date_input("Enter your Date of Birth")
if st.button ("submit"):
 st.write(f"Your Date of birth{selected_Date} has been selected")
 days = (current_Date - selected_Date).days
 years = days / 365.25  # More accurate with leap years
 st.write(f"You are {days} days old.")
 st.write(f"Which is approximately {years:.1f} years.")
