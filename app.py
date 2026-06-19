import streamlit as st
from pathlib import Path
from utils.database import create_table

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Analisis Pola Transaksi Shopee Food",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# MEMBUAT DATABASE OTOMATIS
# =====================================================

create_table()

# =====================================================
# LOAD CSS
# =====================================================

css_file = Path("assets/style.css")

if css_file.exists():
    with open(css_file, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# HEADER
# =====================================================

st.title("🍽️ Analisis Pola Transaksi Shopee Food")

st.markdown("""
### Menggunakan Metode K-Means Clustering

Selamat datang di aplikasi analisis pola transaksi Shopee Food yang dikembangkan
untuk mendukung penelitian skripsi.

Gunakan menu pada **sidebar sebelah kiri** untuk mengakses fitur-fitur aplikasi.
""")

st.divider()

# =====================================================
# FITUR
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
**📂 Kelola Data**

- Tambah data
- Edit data
- Hapus data
- Import CSV
""")

with col2:
    st.success("""
**🤖 K-Means Clustering**

- StandardScaler
- K = 3
- Analisis cluster
""")

with col3:
    st.warning("""
**📊 Hasil Analisis**

- Dashboard
- Visualisasi
- Download CSV
""")

st.divider()

st.caption(
    "© 2026 | Analisis Pola Transaksi Shopee Food Menggunakan Metode K-Means Clustering"
)
