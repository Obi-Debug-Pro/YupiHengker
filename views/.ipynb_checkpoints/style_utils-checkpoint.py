import streamlit as st

def load_css():
    """Inject global CSS styles."""
    st.markdown("""
        <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Outfit', sans-serif;
        }

        /* --- Global Colors & Typography --- */
        h1, h2, h3 {
            color: #1F618D; /* Premium Blue */
            font-weight: 700;
        }
        
        .stMarkdown p {
            font-size: 1.05rem;
            color: #34495E;
            line-height: 1.6;
        }

        /* --- Custom Classes --- */
        
        /* Hero Section Titles */
        .hero-title {
            text-align: center;
            font-size: 3.5rem !important; /* Larger impact */
            font-weight: 800;
            background: -webkit-linear-gradient(45deg, #1F618D, #2E86C1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        
        .hero-subtitle {
            text-align: center;
            font-size: 1.3rem;
            color: #5D6D7E;
            font-weight: 300;
            margin-top: 0;
            margin-bottom: 2rem;
        }

        /* Highlight / Emphasis text */
        .big-font {
            font-size: 1.5rem !important;
            font-weight: 600;
            color: #2E86C1;
        }

        /* Card / Box Styling */
        .quote-box {
            background-color: #F4F6F7;
            padding: 1.5rem;
            border-left: 6px solid #2E86C1;
            border-radius: 8px;
            font-style: italic;
            color: #2C3E50;
            margin: 1rem 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        /* Interactive Elements */
        .stButton button {
            background-color: #2E86C1;
            color: white;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: #1A5276;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        /* Metrics */
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            color: #1F618D;
            font-weight: 700;
        }
        </style>
    """, unsafe_allow_html=True)
    .ipynb_checkpoints/
__pycache__/
*.pyc

