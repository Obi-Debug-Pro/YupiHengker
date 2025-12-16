from pages.data_utils import load_data
import os
import pandas as pd

# Mock streamlit for cache decorator if needed, but since we are running script directly...
# Actually the decorator might fail if streamlit is not running the script? 
# Only if we import 'st'. But data_utils imports st.
# If we run this script with python, 'import streamlit' works but decorator behavior depends on context.
# Usually it just runs the function if not in streamlit context or warns.

try:
    file_path = "c:\\prakbigdata\\YupiHengker\\weather_data.csv"
    print(f"Testing load_data with {file_path}")
    df = load_data(file_path)
    
    print("Columns:", df.columns.tolist())
    print("Head:\n", df.head())
    print("\nData Types:\n", df.dtypes)
    
    # Check specific messy value if known, row 1 had '25.07.00'
    # load_data sets index to DATE.
    # We can check specific row by index if we know the date.
    # The snippet showed '02/01/2023;25.07.00'
    
    target_date = pd.Timestamp('2023-01-02')
    if target_date in df.index:
        val = df.loc[target_date, 'TEMPERATURE']
        print(f"\nValue for {target_date.date()}: {val} (Should be 25.07)")
        assert abs(val - 25.07) < 0.001, "Cleaning failed!"
    else:
        print(f"\nDate {target_date} not found!")

    print("\nSUCCESS: Data loaded and cleaned.")

except Exception as e:
    print(f"\nFAILED: {e}")
