import streamlit as st
import pandas as pd
import datetime

# Page configuration
st.set_page_config(page_title="Mahavir Oil Industry - Daily Prices", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 48px;
            font-weight: 800;
            color: #2c3e50;
            margin-bottom: 0;
        }
        .sub-title {
            text-align: center;
            font-size: 20px;
            color: #7f8c8d;
            margin-top: 0;
        }
        .price-card {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 25px;
            margin: 15px 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .product-name {
            font-size: 24px;
            font-weight: 600;
            color: #34495e;
        }
        .product-price {
            font-size: 28px;
            font-weight: bold;
            color: #27ae60;
        }
        .footer {
            text-align: center;
            color: #95a5a6;
            margin-top: 50px;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-title">Mahavir Oil Industry</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Cotton Seed Cake Price Display</div>', unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; font-size:16px; color:#555;'>📅 Price as on: {datetime.date.today().strftime('%d %B %Y')}</p>", unsafe_allow_html=True)

# Data
varieties = [
    {"name": "Char Ekka", "price": "₹ 2250"},
    {"name": "Double Ghoda", "price": "₹ 2150"},
    {"name": "Pachora Quality", "price": "₹ 2050"}
]

# Show product cards
for item in varieties:
    st.markdown(f"""
        <div class="price-card">
            <div class="product-name">{item['name']}</div>
            <div class="product-price">{item['price']}</div>
        </div>
    """, unsafe_allow_html=True)

# CSV download option
price_df = pd.DataFrame(varieties)
csv = price_df.to_csv(index=False)
st.download_button("📥 Download Price List", csv, "Mahavir_Price_List.csv", "text/csv")

# Footer
st.markdown('<div class="footer">© 2025 Mahavir Oil Industry | Designed for Seller: Sanskar Jain</div>', unsafe_allow_html=True)
