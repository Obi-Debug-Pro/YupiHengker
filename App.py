import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Pendahuluan", icon="🏠"),
    st.Page(page="pages/page2.py", title="Visualisasi Data", icon="📊"),
    st.Page(page="pages/page3.py", title="Pembagian Tugas", icon="⚙️",)
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)


pg.run()