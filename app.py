import streamlit as st

st.set_page_config(
    page_title="Analisis K-Means Shopee Food",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🍽️ Shopee Food Analytics")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    Sistem Analisis Pola Transaksi
    Menggunakan Metode
    K-Means Clustering
    """
)

st.sidebar.markdown("---")

st.sidebar.success(
    """
    📌 Menu tersedia:

    • Dashboard

    • Kelola Data

    • Preprocessing

    • K-Means

    • Hasil

    • Download

    • Tentang
    """
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Universitas Putra Indonesia YPTK Padang"
)

# ==========================================================
# HALAMAN UTAMA
# ==========================================================

st.title("🍽️ Analisis Pola Transaksi Shopee Food")

st.markdown(
    """
    Selamat datang pada aplikasi analisis pola transaksi
    menggunakan algoritma **K-Means Clustering**.

    Gunakan menu pada sidebar untuk berpindah halaman.
    """
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Metode",
        "K-Means"
    )

with col2:
    st.metric(
        "Jumlah Cluster",
        "3"
    )

with col3:
    st.metric(
        "Normalisasi",
        "StandardScaler"
    )

st.markdown("---")

st.subheader("Alur Penggunaan")

st.markdown(
    """
    1. Buka **Kelola Data** dan import dataset CSV.
    2. Jalankan **Preprocessing** untuk membersihkan dan melakukan normalisasi data.
    3. Masuk ke halaman **K-Means** untuk menjalankan proses clustering.
    4. Lihat hasil analisis pada halaman **Hasil**.
    5. Unduh hasil melalui halaman **Download**.
    """
)

st.markdown("---")

st.info(
    """
    Aplikasi ini menggunakan:
    - StandardScaler
    - Elbow Method
    - Silhouette Score
    - K-Means Clustering (K = 3)
    """
)

