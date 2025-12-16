import streamlit as st
import os

from views import page1, page2, page3
from views.style_utils import load_css

st.set_page_config(page_title="YupiHengker", page_icon="🌤", layout="wide")
load_css()

st.sidebar.title("Navigasi")
nav = st.sidebar.radio(
    "Pilih halaman:",
    ["Home", "Pendahuluan", "Visualisasi Data", "Pembagian Tugas"],
)

if nav == "Home":
    st.title("YupiHengker - Aplikasi Analisis Cuaca")
    st.markdown(
        """
        Gunakan menu di sidebar untuk menavigasi ke:
        - Pendahuluan
        - Visualisasi Data
        - Pembagian Tugas
        """
    )

    img_path = os.path.join(os.path.dirname(__file__), "views", "CUACA.png")
    if os.path.exists(img_path):
        st.image(img_path, width=240)
    else:
        st.info("Gambar sampul tidak ditemukan.")
elif nav == "Pendahuluan":
    page1.main()
elif nav == "Visualisasi Data":
    page2.main()
elif nav == "Pembagian Tugas":
    page3.main()