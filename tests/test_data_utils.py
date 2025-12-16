import tempfile
import os
from pages.data_utils import load_data


def test_load_data_cleans_and_parses():
    csv = """DATE;TEMPRATURE;HUMIDITY;RAINFALL
01/01/2023;25.07.00;50;10.05
02/01/2023;20.50;55;05.00
"""

    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "sample.csv")
        with open(p, "w", encoding="utf-8") as f:
            f.write(csv)

        df = load_data(p)

        # Expect two rows and correct index name
        assert len(df) == 2
        assert 'TEMPERATURE' in df.columns
        # First temperature should be cleaned from '25.07.00' -> 25.07
        assert abs(df['TEMPERATURE'].iloc[0] - 25.07) < 1e-6
        # Rainfall parsed
        assert abs(df['RAINFALL'].iloc[0] - 10.05) < 1e-6
