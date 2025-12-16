import os
import pandas as pd


import streamlit as st

@st.cache_data
def load_data(file_path: str):
    """Load and clean weather CSV file.

    - Expects a semicolon-separated CSV with headers like DATE;TEMPRATURE;HUMIDITY;RAINFALL
    - Normalizes header names, renames TEMPRATURE -> TEMPERATURE if present
    - Parses DATE as datetime (format %d/%m/%Y)
    - Cleans numeric fields like '25.07.00' -> 25.07

    Returns a cleaned pandas.DataFrame indexed by DATE.
    """
    if not os.path.exists(file_path):
        return pd.DataFrame(columns=['TEMPERATURE', 'HUMIDITY', 'RAINFALL'])

    df = pd.read_csv(file_path, sep=';')

    df.columns = df.columns.str.upper().str.strip()
    if 'TEMPRATURE' in df.columns:
        df = df.rename(columns={'TEMPRATURE': 'TEMPERATURE'})

    df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y', errors='coerce')
    df = df.dropna(subset=['DATE'])

    for col in ['TEMPERATURE', 'RAINFALL', 'HUMIDITY']:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(r'(\d+\.\d+)\.\d+', r'\1', regex=True)
                .str.replace(',', '.')           
                .str.replace(r'[^0-9\.]', '', regex=True) 
            )
            df[col] = pd.to_numeric(df[col], errors='coerce') 

    df = df.set_index('DATE')
    return df
