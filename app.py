import streamlit as st
from pathlib import Path

# ==========================================================
# KONFIGURASI
# ==========================================================

st.set_page_config(
    page_title="Shopee Food Analytics",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD CSS
# ==========================================================

css_path = Path("assets/style.css")

if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown("## 🍽️ Navigasi")

    st.markdown("")

    st.page_link(
        "app.py",
        label="🏠 Home"
    )

    st.page_link(
        "pages/1_Dashboard.py",
        label="📊 Dashboard"
    )

    st.page_link(
        "pages/2_Kelola_Data.py",
        label="📂 Kelola Data"
    )

    st.page_link(
        "pages/3_Preprocessing.py",
        label="🧹 Preprocessing"
    )

    st.page_link(
        "pages/4_KMeans.py",
        label="🎯 K-Means"
    )

    st.page_link(
        "pages/5_Hasil.py",
        label="📈 Hasil"
    )

    st.page_link(
        "pages/6_Download.py",
        label="⬇️ Download"
    )

    st.page_link(
        "pages/7_Tentang.py",
        label="ℹ️ Tentang"
    )

    st.divider()

    st.markdown("### 📌 Progress")

    progress = 0

    if "scaled_df" in st.session_state:
        progress += 30

    if "hasil_cluster" in st.session_state:
        progress += 70

    st.progress(progress)

    st.caption(f"{progress}% Selesai")

# ==========================================================
# HALAMAN UTAMA
# ==========================================================

st.markdown(
    """
    # 🍽️ Analisis Pola Transaksi Shopee Food

    ### Menggunakan Metode K-Means Clustering

    Aplikasi ini digunakan untuk melakukan analisis pola transaksi
    berdasarkan data pemesanan pada **Buffet The Padang Pasir**
    menggunakan algoritma **K-Means Clustering**.

    ---
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
        ### 📊 Dashboard

        Melihat ringkasan data transaksi,
        statistik, dan visualisasi.
        """
    )

with col2:
    st.info(
        """
        ### 🧹 Preprocessing

        Membersihkan data dan melakukan
        proses StandardScaler.
        """
    )

with col3:
    st.info(
        """
        ### 🎯 K-Means

        Menjalankan Elbow Method,
        Silhouette Score,
        dan proses clustering.
        """
    )

st.markdown("---")

st.subheader("🚀 Langkah Penggunaan")

st.markdown("""
1. Import dataset pada menu **Kelola Data**.
2. Jalankan **Preprocessing**.
3. Jalankan proses **K-Means (K = 3)**.
4. Lihat hasil pada menu **Hasil**.
5. Unduh hasil melalui menu **Download**.
""")

st.success(
    "Aplikasi siap digunakan."
)
