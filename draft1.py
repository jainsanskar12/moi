import streamlit as st
import pandas as pd
import datetime

# Page configuration
st.set_page_config(page_title="Mahavir Oil Industry - Price Board", layout="centered")

# Title section
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #4B8BBE;
            margin-bottom: 5px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #666;
        }
        .card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
    </style>
    <div class="title">Mahavir Oil Industry</div>
    <div class="subtitle">Daily Cotton Seed Cake Price Board</div>
""", unsafe_allow_html=True)

# Current date
today = datetime.date.today().strftime('%d-%b-%Y')
st.markdown(f"**📅 Price as on: {today}**")

# Product prices
price_data = pd.DataFrame({
    "Variety": ["Char Ekka", "Double Ghoda", "Pachora Quality"],
    "Price (₹ per quintal)": [2250, 2150, 2050]
})

# Display styled card with prices
st.markdown('<div class="card">', unsafe_allow_html=True)
st.table(price_data)
st.markdown('</div>', unsafe_allow_html=True)

# Download option
csv = price_data.to_csv(index=False)
st.download_button("📥 Download Price List (CSV)", csv, "mahavir_prices.csv", "text/csv")

# Footer
st.markdown("---")
st.markdown("© 2025 Mahavir Oil Industry | Seller: Sanskar Jain", unsafe_allow_html=True)
