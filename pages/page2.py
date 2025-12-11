import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np 

st.set_page_config(layout="wide") 

st.title("📊 Analisis Tren Data Iklim")
st.subheader("Kota - Periode 2023")

DATA_FILE = 'weather_dataset_sample.csv'

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(DATA_FILE, sep=',') 

        df.columns = df.columns.str.strip().str.upper()
        
        if 'DATE' not in df.columns:
             raise ValueError("Kolom 'DATE' tidak ditemukan. Periksa pemisah CSV.")

        df['DATE'] = pd.to_datetime(df['DATE'], dayfirst=True, errors='coerce')
        df.dropna(subset=['DATE'], inplace=True) 
        
        for col in ['TEMPERATURE', 'HUMIDITY', 'RAINFALL']:
            if col in df.columns: 
                df[col] = (
                    df[col]
                    .astype(str)
                    .str.strip()
                )
                df[col] = pd.to_numeric(df[col], errors='coerce') 
                
        df = df.set_index('DATE')
        return df

    except Exception as e:
        st.error(f"Terjadi kesalahan fatal saat memuat data: {e}. Periksa pemisah CSV dan format data numerik.")
        st.stop()


df_data = load_data()


if df_data.empty:
    st.warning("Data kosong setelah pembersihan. Cek kembali isi CSV Anda.")
    st.stop()

st.success(f"Data {len(df_data)} hari berhasil dimuat dan siap divisualisasi.")

st.markdown("---")

st.sidebar.header("Opsi Visualisasi")

available_vars = [col for col in ['TEMPERATURE', 'HUMIDITY', 'RAINFALL'] if col in df_data.columns]

if not available_vars:
    st.error("Kolom 'TEMPERATURE', 'HUMIDITY', dan 'RAINFALL' tidak ditemukan di CSV Anda.")
    st.stop()

variabel = st.sidebar.selectbox(
    "Pilih Variabel Iklim:",
    available_vars
)


st.subheader(f"Statistik Deskriptif {variabel}")

col1, col2, col3 = st.columns(3)

data_untuk_statistik = df_data[variabel].dropna()

if not data_untuk_statistik.empty:
    with col1:
        st.metric(label=f"Rata-Rata {variabel}", value=f"{data_untuk_statistik.mean():.2f}")
    with col2:
        st.metric(label=f"{variabel} Maksimum", value=f"{data_untuk_statistik.max():.2f}")
    with col3:
        st.metric(label=f"{variabel} Minimum", value=f"{data_untuk_statistik.min():.2f}")
else:
     st.warning(f"Data valid untuk {variabel} tidak ditemukan untuk dihitung statistiknya.")

st.subheader(f"Tren Harian {variabel}")


fig = px.line(
    df_data.dropna(subset=[variabel]),
    y=variabel,
    title=f"Tren Harian {variabel}"
)

fig.update_layout(
    xaxis_title="Tanggal",
    yaxis_title=variabel,
)

st.plotly_chart(fig, use_container_width=True)