import os
import streamlit as st
import plotly.express as px
import pandas as pd
from views.data_utils import load_data

def render_overview(df):
    """Render Key Metrics and Overview"""
    st.header("📈 Ringkasan Eksekutif")
    st.caption("Gambaran umum kondisi rata-rata selama periode 2023.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        avg_temp = df['TEMPERATURE'].mean()
        st.metric("Rerata Suhu", f"{avg_temp:.2f} °C", help="Rata-rata suhu harian")
    with col2:
        avg_hum = df['HUMIDITY'].mean()
        st.metric("Rerata Kelembapan", f"{avg_hum:.2f} %", help="Rata-rata kelembapan relatif")
    with col3:
        avg_rain = df['RAINFALL'].mean()
        total_rain = df['RAINFALL'].sum()
        st.metric("Total Curah Hujan", f"{total_rain:.2f} mm", help="Total akumulasi curah hujan")

    st.markdown("---")
    st.info("Gunakan menu **'Analisis Tren'** di sidebar untuk melihat grafik detail waktu ke waktu.")

def render_trends(df):
    """Render Time Series Charts + Interpretasi"""
    st.header("📉 Analisis Tren Waktu")
    
    variables = st.multiselect(
        "Pilih Variabel:",
        ['TEMPERATURE', 'HUMIDITY', 'RAINFALL'],
        default=['TEMPERATURE']
    )

    if not variables:
        st.warning("Pilih setidaknya satu variabel untuk ditampilkan.")
        return

    fig_line = px.line(
        df.reset_index(),
        x='DATE',
        y=variables,
        title="Dinamika Cuaca Harian",
        markers=True,
        color_discrete_sequence=px.colors.qualitative.G10
    )
    fig_line.update_layout(
        hovermode="x unified",
        xaxis_title="Tanggal",
        yaxis_title="Nilai",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("### 📝 Interpretasi Analisis Tren")

    if "TEMPERATURE" in variables:
        st.info(
            "🌡️ **Temperatur** menunjukkan fluktuasi harian yang cukup tinggi, "
            "namun tetap berada dalam rentang yang relatif stabil sepanjang tahun 2023. "
            "Tidak terlihat tren kenaikan atau penurunan ekstrem, "
            "mengindikasikan karakteristik iklim tropis yang konsisten."
        )

    if "HUMIDITY" in variables:
        st.info(
            "💧 **Kelembapan** memperlihatkan variabilitas yang cukup tajam sepanjang waktu. "
            "Perubahan ini mencerminkan dinamika atmosfer yang dipengaruhi oleh "
            "pola hujan dan kondisi cuaca harian."
        )

    if "RAINFALL" in variables:
        st.info(
            "🌧️ **Curah hujan** menunjukkan pola yang tidak merata dan bersifat episodik. "
            "Lonjakan hujan pada periode tertentu mengindikasikan potensi "
            "kejadian cuaca ekstrem seperti banjir."
        )

    
        st.warning("Pilih setidaknya satu variabel untuk ditampilkan.")

def render_analysis(df):
    """Render Advanced Analysis (Correlation, Distribution)"""
    st.header("🔥 Hubungan & Distribusi Data")
    
    tab1, tab2 = st.tabs(["Korelasi", "Distribusi"])
    
    with tab1:
        st.subheader("Matriks Korelasi")
        if not df.empty:
            corr = df[['TEMPERATURE', 'HUMIDITY', 'RAINFALL']].corr()
            fig_corr = px.imshow(
                corr,
                text_auto=True,
                aspect="auto",
                color_continuous_scale="RdBu_r",
                title="Korelasi Pearson Antar Variabel"
            )
            st.plotly_chart(fig_corr, use_container_width=True)
            st.caption("Ket: Nilai mendekati 1 berarti korelasi positif kuat, -1 negatif kuat.")
            st.info("""
📌 **Interpretasi Korelasi:**

Seluruh pasangan variabel memiliki nilai korelasi mendekati nol.
Hal ini menunjukkan **tidak adanya hubungan linier yang kuat**
antara suhu, kelembapan, dan curah hujan sepanjang tahun 2023.

Seluruh pasangan variabel memiliki nilai korelasi mendekati nol.
Hal ini menunjukkan **tidak adanya hubungan linier yang kuat**
antara suhu, kelembapan, dan curah hujan sepanjang tahun 2023.
""")

   
    with tab2:
        st.subheader("Histogram Distribusi")
        
        dist_var = st.selectbox(
            "Pilih Variabel:",
            ['TEMPERATURE', 'HUMIDITY', 'RAINFALL']
        )
        
        fig_dist = px.histogram(
            df,
            x=dist_var,
            nbins=30,
            marginal="box",
            title=f"Distribusi Frekuensi {dist_var}",
            color_discrete_sequence=['#EF553B']
        )
        st.plotly_chart(fig_dist, use_container_width=True)

        st.markdown("### 📝 Interpretasi Distribusi Data")

        if dist_var == "TEMPERATURE":
            st.info(
                "🌡️ **Distribusi Temperatur** terkonsentrasi pada nilai menengah "
                "dengan sebaran relatif simetris, menunjukkan kondisi suhu yang stabil "
                "dan minim kejadian ekstrem."
            )

        elif dist_var == "HUMIDITY":
            st.info(
                "💧 **Distribusi Kelembapan** menunjukkan sebaran yang cukup lebar, "
                "mengindikasikan variabilitas atmosfer yang tinggi sepanjang tahun."
            )

        elif dist_var == "RAINFALL":
            st.info(
                "🌧️ **Distribusi Curah Hujan** bersifat tidak merata dan condong "
                "pada nilai rendah dengan beberapa lonjakan ekstrem, "
                "menunjukkan hujan yang episodik."
            )


def render_data(df):
    """Render Raw Data Table"""
    st.header("📂 Data Mentah")
    
    with st.expander("Klik untuk melihat tabel", expanded=True):
        st.dataframe(df.style.background_gradient(cmap="Blues"), use_container_width=True)
        
    csv = df.to_csv(sep=';').encode('utf-8')
    st.download_button(
        "📥 Download CSV",
        csv,
        "weather_data_filtered.csv",
        "text/csv",
        key='download-csv'
    )

def main():
    st.set_page_config(layout="wide") if not st.session_state.get('is_main_config_set') else None
    st.title("� Dashboard Iklim & Cuaca")
    
    DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "weather_data.csv")
    df_raw = load_data(DATA_FILE)
    
    if df_raw.empty:
        st.error("Data tidak ditemukan.")
        return

    st.sidebar.title("Navigasi")
    
    view_mode = st.sidebar.radio(
        "Pilih Menu:",
        ["Ringkasan", "Analisis Tren", "Korelasi & Distribusi", "Data Mentah"]
    )
    
    st.sidebar.markdown("---")
    st.sidebar.header("🎛️ Filter Data")
    
    min_d, max_d = df_raw.index.min().date(), df_raw.index.max().date()
    date_range = st.sidebar.date_input(
        "Periode Waktu:",
        value=(min_d, max_d),
        min_value=min_d,
        max_value=max_d
    )
    
    if len(date_range) == 2:
        start_d, end_d = date_range
        mask = (df_raw.index >= pd.Timestamp(start_d)) & (df_raw.index <= pd.Timestamp(end_d))
        df_filtered = df_raw.loc[mask]
    else:
        df_filtered = df_raw

    st.sidebar.info(f"Data: {len(df_filtered)} baris")

    if view_mode == "Ringkasan":
        render_overview(df_filtered)
    elif view_mode == "Analisis Tren":
        render_trends(df_filtered)
    elif view_mode == "Korelasi & Distribusi":
        render_analysis(df_filtered)
    elif view_mode == "Data Mentah":
        render_data(df_filtered)

if __name__ == "__main__":
    main()