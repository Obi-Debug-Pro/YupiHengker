import streamlit as st

st.title("Welcome to the YupiHengker's Home Page")
st.write("This the main landing page of the app.")


# --- Konfigurasi Halaman (Pertahankan) ---
st.set_page_config(
    page_title="Analisis Cuaca Kelompok 1",
    page_icon="☀️",
    layout="wide"
)

# --- Judul dan Pengantar ---
st.title("☀️ Proyek Analisis Iklim dan Cuaca")

st.subheader("Pendahuluan dan Latar Belakang Proyek")

st.markdown("""
Selamat datang di aplikasi visualisasi data iklim Kelompok 1. Aplikasi ini merupakan luaran dari analisis data iklim historis menggunakan Python dan Streamlit.

Iklim, sesungguhnya, adalah narasi abadi di kanvas geografi. Ia bukan sekadar deretan angka statistik, ia adalah pergantian babak yang menentukan nasib agraria dan rima harian manusia. Setiap hembusan angin adalah bisikan sejarah, setiap tetes hujan adalah alinea basah yang menuturkan keindahan sekaligus ancaman. Maka, menelaah data cuaca adalah upaya kita membaca manuskrip alam, memahami diksi perubahannya yang kini semakin cepat, demi merencanakan simfoni kehidupan yang berkelanjutan.

Namun, setiap puisi agung memerlukan tangan arsitek untuk mengukur rima dan alurnya. Setelah merasakan getaran metaforis dari langit, kita harus menyelam ke dalam disiplin data. Proyek ini adalah jembatan antara ilusi dan presisi, upaya kami mengubah bisikan angin dan tangis hujan menjadi notasi statistik yang terstruktur. Dengan Python dan Streamlit, kami menarik narasi cuaca dari kabut ketidakpastian, memahatnya menjadi grafik yang jernih, agar kita dapat merencanakan bukan hanya musim yang akan datang, tetapi juga warisan iklim bagi generasi esok.
""")
st.image("0bd2766f7359298e6a7174efc3b40825.jpg", caption="Kelompok yupi anak senja", width=300)

st.markdown("""
### 1. Urgensi Data Cuaca dan Iklim

Data cuaca memiliki peran sentral yang semakin krusial, terutama di tengah isu perubahan iklim global. Analisis terhadap tren iklim historis diperlukan untuk:
* **Mitigasi Bencana:** Mengidentifikasi pola ekstrem, seperti curah hujan tinggi yang berpotensi menyebabkan banjir, memungkinkan pemerintah daerah melakukan perencanaan mitigasi yang lebih baik.
* **Sektor Ekonomi Vital:** Data suhu dan kelembapan adalah penentu utama keberhasilan sektor pertanian. Selain itu, sektor energi dan transportasi juga sangat bergantung pada prediksi dan tren cuaca jangka panjang.
* **Perencanaan Infrastruktur:** Pengetahuan tentang variasi iklim membantu dalam mendesain infrastruktur yang tahan terhadap perubahan suhu ekstrem dan intensitas hujan.

### 2. Tujuan Proyek dan Metodologi

Proyek ini bertujuan tidak hanya untuk menampilkan data, tetapi juga untuk menyajikan temuan secara interaktif dan mudah diakses. Tujuan utama kami meliputi:

1.  **Pengolahan Data Historis:** Mengolah data mentah yang didapatkan dari sumber tepercaya (misalnya BMKG) untuk menghasilkan metrik yang valid.
2.  **Visualisasi Interaktif:** Menyajikan tren tahunan suhu, kelembapan, dan curah hujan melalui grafik interaktif menggunakan Streamlit dan *library* visualisasi Python.
3.  **Analisis Deskriptif Sederhana:** Menghitung dan menampilkan statistik utama seperti nilai rata-rata, maksimum, dan minimum dari variabel cuaca.
""")

st.markdown("---")

# --- Petunjuk Navigasi dan Identitas ---
st.info("Silakan navigasi ke menu **'Visualisasi Data'** di sisi kiri untuk melihat hasil analisis data iklim kami.")

st.subheader("Disusun Oleh Kelompok 1:")
st.text("""
- [Naufal Rafi Putera Wiyanto]
- [Nazil Dwi Khoirul Fata]
- [Mumammad Fadhil Fatkhurrohman]
- [Obinata Ridho Abdillah]
""")