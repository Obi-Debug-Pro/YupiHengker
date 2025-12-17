import streamlit as st


def main():
    st.title("👥 Pembagian Tugas Anggota Kelompok")
    st.markdown("---")

    st.info("Berikut adalah kontribusi setiap anggota dalam pengembangan proyek ini:")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👨‍💻 Naufal Rafi Putera")
        st.write("• Pencarian Data Mentah")
        st.write("• Testing & Validasi")

        st.subheader("👨‍💻 Nazil Dwi Khoirul Fata")
        st.write("• Pengumpulan & Pembersihan Data")
        st.write("• Dokumentasi Teknis")

    with col2:
        st.subheader("👨‍💻 Muhammad Fadhil Fatkhurrohman")
        st.write("•  Analisis Data & VisualisasiX")
        st.write("• Pengembangan Streamlit")

        st.subheader("👨‍💻 Obinata Ridho Abdillah")
        st.write("• Manajemen Proyek")
        st.write("• Integrasi Sistem")

    st.success("Solid work from the team! 🚀")


if __name__ == "__main__":
    main()
