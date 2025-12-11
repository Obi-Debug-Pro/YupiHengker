import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")
st.title("📊 Analisis Tren Data Iklim")
st.subheader("Periode 2023")

DATA_FILE = 'weather_dataset_sample.csv'

@st.cache_data
def load_data():
    try:
        df_raw = pd.read_csv(DATA_FILE, sep=',')
        df = df_raw.copy()

        df.columns = df.columns.str.strip().str.upper()

        if 'DATE' not in df.columns:
            raise ValueError("Kolom 'DATE' tidak ditemukan. Periksa pemisah CSV.")

        df['DATE'] = pd.to_datetime(df['DATE'], format='%m/%d/%Y', errors='coerce')
        df.dropna(subset=['DATE'], inplace=True)

        for col in ['TEMPERATURE', 'HUMIDITY', 'RAINFALL']:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()
                df[col] = pd.to_numeric(df[col], errors='coerce')

        df = df.set_index('DATE')
        return df_raw, df

    except Exception as e:
        st.error(f"Terjadi kesalahan fatal saat memuat data: {e}.")
        st.stop()

# Load data
df_raw, df_data = load_data()

# Diagnostik Awal
st.write("Jumlah baris asli dari CSV:", len(df_raw))
st.write("Jumlah baris setelah parsing tanggal:", len(df_data))
st.write("Jumlah tanggal unik:", df_data.index.nunique())

with st.expander("📄 Diagnostik Data Mentah"):
    if 'DATE' in df_raw.columns:
        st.write("Contoh 10 nilai DATE mentah:", df_raw['DATE'].head(10))
    gagal_parsing = len(df_raw) - len(df_data)
    st.write("Perkiraan jumlah DATE gagal parsing:", gagal_parsing)

    for kolom in ['TEMPERATURE', 'HUMIDITY', 'RAINFALL']:
        if kolom in df_data.columns:
            st.write(f"Jumlah nilai kosong di kolom {kolom}:", df_data[kolom].isna().sum())

if df_data.empty:
    st.warning("Data kosong setelah pembersihan. Cek kembali isi CSV Anda.")
    st.stop()

st.success(f"Data {len(df_data)} hari berhasil dimuat dan siap divisualisasi.")
st.markdown("---")

# Filter Sidebar
st.sidebar.header("Filter Data")

df_data['YEAR'] = df_data.index.year
df_data['MONTH'] = df_data.index.strftime('%B')

month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

selected_years = st.sidebar.multiselect("Pilih Tahun:", options=sorted(df_data['YEAR'].unique()), default=sorted(df_data['YEAR'].unique()))
selected_months_name = st.sidebar.multiselect("Pilih Bulan:", options=month_order, default=month_order)
selected_months_num = [month_order.index(m) + 1 for m in selected_months_name]

df_filtered = df_data[
    (df_data.index.year.isin(selected_years)) &
    (df_data.index.month.isin(selected_months_num))
]

with st.expander("📊 Diagnostik Setelah Filter"):
    st.write("Jumlah data setelah filter tahun & bulan:", len(df_filtered))
    st.write("Tanggal awal:", df_filtered.index.min())
    st.write("Tanggal akhir:", df_filtered.index.max())

df_filtered = df_filtered.drop(columns=['YEAR', 'MONTH'], errors='ignore')

# Visualisasi Sidebar
st.sidebar.header("Opsi Visualisasi")

available_vars = [col for col in ['TEMPERATURE', 'HUMIDITY', 'RAINFALL'] if col in df_filtered.columns]
if not available_vars:
    st.error("Kolom iklim tidak ditemukan di CSV Anda.")
    st.stop()

variabel = st.sidebar.selectbox("Pilih Variabel Iklim:", available_vars)
chart_type = st.sidebar.radio("Pilih Jenis Grafik:", ["Line Chart", "Bar Chart", "Area Chart"])

# Statistik Deskriptif
st.subheader(f"Statistik Deskriptif {variabel}")
col1, col2, col3 = st.columns(3)
data_untuk_statistik = df_filtered[variabel].dropna()

if not data_untuk_statistik.empty:
    col1.metric(f"Rata-Rata {variabel}", f"{data_untuk_statistik.mean():.2f}")
    col2.metric(f"{variabel} Maksimum", f"{data_untuk_statistik.max():.2f}")
    col3.metric(f"{variabel} Minimum", f"{data_untuk_statistik.min():.2f}")
else:
    st.warning(f"Data valid untuk {variabel} tidak ditemukan.")

# Grafik Tren Harian
st.subheader(f"Tren Harian {variabel}")
df_plot = df_filtered.dropna(subset=[variabel])

if chart_type == "Line Chart":
    fig = px.line(df_plot, x=df_plot.index, y=variabel, title=f"{chart_type} {variabel}", markers=True)
elif chart_type == "Bar Chart":
    fig = px.bar(df_plot, x=df_plot.index, y=variabel, title=f"{chart_type} {variabel}")
elif chart_type == "Area Chart":
    fig = px.area(df_plot, x=df_plot.index, y=variabel, title=f"{chart_type} {variabel}")

fig.update_layout(
    xaxis_title="Tanggal",
    yaxis_title=variabel,
    xaxis=dict(tickformat="%b %Y", tickangle=-45, showgrid=True),
    yaxis=dict(showgrid=True),
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

