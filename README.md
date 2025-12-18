# 🌤️ YupiHengker - Analisis Iklim & Cuaca

> *"Sebuah kumpulan narasi digital yang merangkum upaya kolektif YupiHengker. Layaknya bait-bait epik yang disusun hati-hati, repository ini menyimpan jejak proses kreatif kami, dari draf awal hingga finalisasi. Inilah arsip abadi yang menuturkan kisah sebuah proyek."*

## 📖 Tentang Proyek

**YupiHengker** adalah aplikasi *dashboard* interaktif yang dibangun menggunakan **Python** dan **Streamlit**. Aplikasi ini bertujuan untuk mempermudah analisis data cuaca historis (Suhu, Kelembapan, Curah Hujan) melalui visualisasi modern yang intuitif.

Proyek ini dirancang untuk memberikan wawasan mendalam mengenai pola iklim, membantu dalam mitigasi bencana, serta mendukung sektor ekonomi yang bergantung pada cuaca.

---

## 🚀 Fitur Utama

✅ **Dashboard Interaktif**: Halaman utama dengan statistik *real-time* dan navigasi berbasis kartu.
✅ **Analisis Multi-Variabel**: Bandingkan tren Suhu, Kelembapan, dan Curah Hujan dalam satu grafik dinamis.
✅ **Eksplorasi Data**: Filter data berdasarkan rentang tanggal spesifik.
✅ **Korelasi & Statistik**: Heatmap korelasi Pearson dan histogram distribusi data.
✅ **Desain Responsif**: Antarmuka modern dengan tipografi premium dan tata letak yang rapi.
✅ **Ekspor Data**: Unduh hasil filter data dalam format CSV.

---

## 🛠️ Teknologi yang Digunakan

-   **Bahasa**: Python 3.10+
-   **Framework UI**: [Streamlit](https://streamlit.io/)
-   **Visualisasi**: Plotly Express
-   **Manipulasi Data**: Pandas
-   **Styling**: Custom CSS (Google Fonts 'Outfit')

---

## 📦 Struktur Proyek

```bash
YupiHengker/
├── App.py                  # Entry point aplikasi (Home Page & Routing)
├── requirements.txt        # Daftar dependensi library
├── weather_data.csv        # Dataset utama
├── views/                  # Modul Halaman (Refactored from 'pages')
│   ├── page1.py            # Pendahuluan & Latar Belakang
│   ├── page2.py            # Visualisasi & Analisis Data
│   ├── page3.py            # Profil Tim Pengembang
│   ├── data_utils.py       # Helper: Load & Clean Data
│   └── style_utils.py      # Helper: Global CSS Styling
└── README.md               # Dokumentasi Proyek
```

> **Catatan**: Folder `views/` digunakan menggantikan `pages/` default Streamlit untuk menonaktifkan navigasi sidebar otomatis, memberikan kontrol penuh pada menu kustom kami.

---

## 💻 Cara Menjalankan

1.  **Clone Repository**
    ```bash
    git clone https://github.com/username/YupiHengker.git
    cd YupiHengker
    ```

2.  **Buat Virtual Environment (Opsional tapi Disarankan)**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependensi**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi**
    ```bash
    streamlit run App.py
    ```

---

## 👥 Tim Pengembang (Kelompok 1)

| Nama | Peran |
| :--- | :--- |
| **Naufal Rafi Putera** | Pencarian Data Mentah , testing & validasi |
| **Nazil Dwi Khoirul Fata** | Pengumpulan Data , Pembersihan Data & Dokumentasi Teknis |
| **Muhammad Fadhil Fatkhurrohman** | Analisis Data , Visualisasi & Pengembangan Fitur Sytreamlit|
| **Obinata Ridho Abdillah** | Manajemen Proyek & Integrasi |

---
*© 2024 YupiHengker Team. Dibuat dengan ❤️ dan ☕.*
