import streamlit as st
import pandas as pd
import plotly.express as px 
import matplotlib.pyplot as plt

st.title("📊 Analisis Tren Data Iklim")
st.subheader("Kota - Periode 2023")

DATA_FILE = 'weather_data.csv'

@st.cache_data
@st.cache_data
def load_data():
    try:
        # Gunakan delimiter ; 
        df = pd.read_csv(DATA_FILE, sep=';')

        # Konversi DATE ke datetime
        df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y')

        # Bersihkan nilai seperti 25.07.00 → 25.07
        for col in ['TEMPRATURE', 'RAINFALL']:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(r'(\d+\.\d+)\.\d+', r'\1', regex=True)
                .astype(float)
            )

        # Set sebagai index
        df = df.set_index('DATE')
        return df

    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses data: {e}. Cek format CSV Anda.")
        st.stop()



df_data = load_data()

st.success(f"Data {len(df_data)} hari berhasil dimuat dan siap divisualisasi.")

st.markdown("---")


st.sidebar.header("Opsi Visualisasi")
variabel = st.sidebar.selectbox(
    "Pilih Variabel Iklim:",
    ['TEMPERATURE', 'HUMIDITY', 'RAINFALL']
)


st.subheader(f"Statistik Deskriptif {variabel}")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label=f"Rata-Rata {variabel}", value=f"{df_data[variabel].mean():.2f}")
with col2:
    st.metric(label=f"{variabel} Maksimum", value=f"{df_data[variabel].max():.2f}")
with col3:
    st.metric(label=f"{variabel} Minimum", value=f"{df_data[variabel].min():.2f}")



st.subheader(f"Tren Harian {variabel}")


fig = px.line(
    df_data,
    y=variabel,
    title=f"Tren Harian {variabel}"
)
st.plotly_chart(fig, use_container_width=True)