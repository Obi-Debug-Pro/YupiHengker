import streamlit as st
import os
import pandas as pd
from views import page1, page2, page3
from views.style_utils import load_css
from views.data_utils import load_data

st.set_page_config(page_title="YupiHengker", page_icon="🌤", layout="wide")
load_css()

# --- Sidebar Navigation ---
st.sidebar.title("Navigasi")
nav = st.sidebar.radio(
    "Menu Utama:",
    ["Home", "Pendahuluan", "Visualisasi Data", "Tim Pengembang"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.caption("© 2024 YupiHengker Team")

# --- Content Routing ---
if nav == "Home":
    # Hero Section
    col_logo, col_text = st.columns([1, 2])
    
    with col_logo:
        img_path = os.path.join(os.path.dirname(__file__), "views", "CUACA.png")
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.warning("Cover image not found.")

    with col_text:
        st.markdown('<h1 class="hero-title" style="text-align: left;">YupiHengker</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle" style="text-align: left;">Platform Analisis Iklim Cerdas & Interaktif</p>', unsafe_allow_html=True)
        st.write("""
        Selamat datang di dashboard cuaca modern kami. Aplikasi ini dirancang untuk menyajikan 
        wawasan mendalam dari data iklim historis melalui visualisasi yang interaktif dan mudah dipahami.
        """)
        if st.button("🚀 Mulai Eksplorasi Data"):
            # Simple way to hint user or reload (Streamlit limitation on nav jump without extra logic)
            st.markdown("*Silakan pilih menu 'Visualisasi Data' di sidebar.*")

    st.markdown("---")

    # Quick Stats Section
    st.subheader("⚡ Kilas Data Terkini")
    
    # Try loading data for quick stats
    try:
        DATA_FILE = os.path.join(os.path.dirname(__file__), "weather_data.csv")
        df = load_data(DATA_FILE)
        
        if not df.empty:
            latest_date = df.index.max()
            latest_row = df.loc[latest_date]
            
            s1, s2, s3, s4 = st.columns(4)
            s1.metric("Data Terakhir", latest_date.strftime("%d %b %Y"))
            s2.metric("Suhu", f"{latest_row['TEMPERATURE']} °C")
            s3.metric("Kelembapan", f"{latest_row['HUMIDITY']} %")
            s4.metric("Curah Hujan", f"{latest_row['RAINFALL']} mm")
        else:
            st.info("Data cuaca belum tersedia.")
            
    except Exception:
        st.error("Gagal memuat ringkasan data.")

    st.markdown("---")

    # Feature Cards
    st.subheader("📌 Fitur & Menu")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="quote-box">
        <h4>📖 Pendahuluan</h4>
        <p>Latar belakang, urgensi, dan metodologi proyek kami.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="quote-box">
        <h4>📊 Visualisasi Data</h4>
        <p>Grafik interaktif, peta panas, dan analisis tren lengkap.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="quote-box">
        <h4>👥 Tim Pengembang</h4>
        <p>Kenalan dengan anggota kelompok 1 di balik proyek ini.</p>
        </div>
        """, unsafe_allow_html=True)

elif nav == "Pendahuluan":
    page1.main()
elif nav == "Visualisasi Data":
    page2.main()
elif nav == "Tim Pengembang":
    page3.main()