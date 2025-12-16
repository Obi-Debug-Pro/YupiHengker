import streamlit as st


def main():
    st.title("👥 Pembagian Tugas Anggota Kelompok")
    st.markdown("---")

    st.info("Berikut adalah kontribusi setiap anggota dalam pengembangan proyek ini:")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👨‍💻 Naufal Rafi Putera Wiyanto")
        st.write("• Analisis Data & Visualisasi")
        st.write("• Pengembangan Fitur Streamlit")

        st.subheader("👨‍💻 Nazil Dwi Khoirul Fata")
        st.write("• Pengumpulan & Pembersihan Data")
        st.write("• Dokumentasi Teknis")

    with col2:
        st.subheader("👨‍💻 Mumammad Fadhil Fatkhurrohman")
        st.write("• Desain UI/UX")
        st.write("• Testing & Validasi")

        st.subheader("👨‍💻 Obinata Ridho Abdillah")
        st.write("• Manajemen Proyek")
        st.write("• Integrasi Sistem")

    st.success("Solid work from the team! 🚀")


if __name__ == "__main__":
    main()
