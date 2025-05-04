import streamlit as st
import pandas as pd
import datetime

# Page configuration
st.set_page_config(page_title="Mahavir Oil Industries - Daily Prices", layout="centered")

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
        .section-title {
            font-size: 24px;
            font-weight: bold;
            color: #34495e;
            margin-top: 40px;
        }
        .product-name {
            font-size: 20px;
            font-weight: 600;
            color: #34495e;
        }
        .product-price {
            font-size: 22px;
            font-weight: bold;
            color: #27ae60;
        }
        .contact-info {
            font-size: 16px;
            color: #2c3e50;
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
st.markdown('<div class="main-title">Mahavir Oil Industries</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Cotton Seed Cake Price Display</div>', unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; font-size:16px; color:#555;'>📅 Price as on: {datetime.date.today().strftime('%d %B %Y')}</p>", unsafe_allow_html=True)

# Company Overview
st.markdown('<div class="section-title">🏢 Company Overview</div>', unsafe_allow_html=True)
st.write("""
Mahavir Oil Industries is a leading manufacturer and supplier of high-quality cotton seed cake. With years of experience in the industry, we are committed to providing our customers with the best products and services.
""")

# Product Details
st.markdown('<div class="section-title">🛍️ Product Details</div>', unsafe_allow_html=True)

products = [
    {"name": "Char Ekka", "price": "₹ 2250", "description": "Premium quality cotton seed cake with high protein content."},
    {"name": "Double Ghoda", "price": "₹ 2150", "description": "High-grade cotton seed cake suitable for livestock feed."},
    {"name": "Pachora Quality", "price": "₹ 2050", "description": "Economical cotton seed cake with balanced nutrients."}
]

for product in products:
    st.markdown(f"**{product['name']}**")
    st.write(f"{product['description']}")
    st.markdown(f"<span class='product-price'>{product['price']}</span>", unsafe_allow_html=True)
    st.markdown("---")

# Contact Information
st.markdown('<div class="section-title">📞 Contact Information</div>', unsafe_allow_html=True)
st.markdown("""
<div class='contact-info'>
<strong>Address:</strong> Shendurni, Maharashtra, India<br>

<strong>Email:</strong> vkkshendurni111@gmail.com
</div>
""", unsafe_allow_html=True)

# Image Gallery
st.markdown('<div class="section-title">🖼️ Image Gallery</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">© 2025 Mahavir Oil Industries | Designed for Seller: Sanskar Jain</div>', unsafe_allow_html=True)
