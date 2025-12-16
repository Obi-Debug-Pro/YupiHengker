import streamlit as st
import os


def main():
    # --- Global CSS handles styling now ---

    # --- Hero Section ---
    st.markdown('<p class="hero-title">☀️ Proyek Analisis Iklim</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Eksplorasi Data Cuaca Historis & Dampaknya</p>', unsafe_allow_html=True)
    st.markdown("---")

    col_hero1, col_hero2 = st.columns([1, 2])
    
    with col_hero1:
        img_path = os.path.join(os.path.dirname(__file__), "CUACA.png")
        if os.path.exists(img_path):
            st.image(img_path, caption="Ilustrasi Cuaca", use_container_width=True)
        else:
            st.markdown("📷 *Gambar Cover*")
    
    with col_hero2:
        st.subheader("Latar Belakang")
        st.markdown("""
        <div class="quote-box">
        "Iklim adalah narasi abadi...' menelaah data cuaca adalah upaya kita membaca manuskrip alam, 
        memahami diksi perubahannya yang kini semakin cepat."
        </div>
        """, unsafe_allow_html=True)
        st.write("""
        Selamat datang di aplikasi visualisasi data iklim Kelompok 1. Proyek ini menjembatani **ilusi dan presisi**, 
        mengubah data mentah menjadi wawasan bermakna untuk masa depan yang berkelanjutan.
        """)

    # --- Urgensi Section with Columns ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center;">Mengapa Data Iklim Penting?</h3>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 🛡️ Mitigasi Bencana")
        st.info("Mengidentifikasi pola ekstrem untuk perencanaan mitigasi banjir dan bencana alam.")

    with col2:
        st.markdown("#### 🌾 Ekonomi Vital")
        st.success("Menentukan keberhasilan sektor pertanian dan energi yang bergantung pada cuaca.")

    with col3:
        st.markdown("#### 🏗️ Infrastruktur")
        st.warning("Desain bangunan tahan perubahan suhu dan intensitas hujan ekstrem.")

    # --- Metodologi ---
    st.markdown("---")
    st.subheader("🎯 Tujuan & Metodologi")
    
    with st.expander("Baca lebih lanjut tentang metodologi kami", expanded=False):
        st.markdown("""
        1.  **Pengolahan Data Historis**: Pembersihan data mentah (BMKG) menjadi dataset valid.
        2.  **Visualisasi Interaktif**: Grafik dinamis untuk tren suhu, kelembapan, dan hujan.
        3.  **Analisis Deskriptif**: Statistik utama (Rata-rata, Min, Max).
        """)

    # --- Footer / CTA ---
    st.markdown("<br>", unsafe_allow_html=True)
    st.success("👉 Mulai eksplorasi di menu **'Visualisasi Data'** (Sidebar kiri).")

    st.markdown("---")
    st.caption("Disusun Oleh Kelompok 1: Naufal Rafi, Nazil Dwi, Muhammad Fadhil, Obinata Ridho.")


if __name__ == "__main__":
    main()