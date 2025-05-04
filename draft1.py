import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Mahavir Oil Industry - Daily Cotton Seed Cake Prices", layout="centered")

st.title("🌾 Mahavir Oil Industry")
st.subheader("Daily Cotton Seed Cake Price Tracker")

# Initialize session state to store data
if 'price_data' not in st.session_state:
    st.session_state.price_data = pd.DataFrame(columns=['Date', 'Price (₹ per quintal)'])

# Input form
with st.form("price_form"):
    date = st.date_input("Select Date", datetime.date.today())
    price = st.number_input("Enter Price (₹ per quintal)", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Submit Price")

    if submitted:
        new_entry = pd.DataFrame([[date, price]], columns=['Date', 'Price (₹ per quintal)'])
        st.session_state.price_data = pd.concat([st.session_state.price_data, new_entry], ignore_index=True)
        st.success("Price added successfully!")

# Sort data by date
st.session_state.price_data.sort_values("Date", inplace=True)

# Show table
st.write("### 📊 Price History")
st.dataframe(st.session_state.price_data, use_container_width=True)

# Plot
st.write("### 📈 Price Trend")
st.line_chart(st.session_state.price_data.set_index("Date"))

# Option to download CSV
csv = st.session_state.price_data.to_csv(index=False)
st.download_button("Download Data as CSV", csv, "cotton_seed_prices.csv", "text/csv")

