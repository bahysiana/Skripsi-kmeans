import streamlit as st

st.set_page_config(
    page_title="Tentang",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ Tentang Aplikasi")

st.markdown("---")

st.header("Deskripsi")

st.write("""
Aplikasi ini dibuat untuk melakukan analisis pola transaksi Shopee Food
menggunakan metode K-Means Clustering berdasarkan data pemesanan
pada Toko Buffet The Padang Pasir.
""")

st.markdown("---")

st.header("Fitur Aplikasi")

st.markdown("""
- Dashboard Ringkasan Data
- Kelola Data (CRUD)
- Import Dataset CSV
- Preprocessing Data
- StandardScaler
- Elbow Method
- Silhouette Score
- K-Means Clustering (K = 3)
- Visualisasi Hasil Clustering
- Download Hasil Analisis
""")

st.markdown("---")

st.header("Metode")

st.markdown("""
Metode yang digunakan pada aplikasi ini:

1. Data Cleaning
2. StandardScaler
3. Elbow Method
4. Silhouette Score
5. K-Means Clustering
6. Visualisasi Hasil Cluster
""")

st.markdown("---")

st.header("Variabel Clustering")

st.table({
    "Variabel": [
        "Total_harga",
        "Jumlah_pesanan",
        "rata_rata_harga",
        "waktu_persiapan_yang_diberikan",
        "waktu_persiapan_digunakan"
    ]
})

st.markdown("---")

st.header("Informasi")

st.info("""
Program ini dikembangkan sebagai implementasi penelitian
Analisis Pola Transaksi Shopee Food Menggunakan Metode
K-Means Clustering Berdasarkan Data Pemesanan
Pada Toko Buffet The Padang Pasir.
""")

st.markdown("---")

st.caption("© 2026 - Sistem Analisis K-Means Shopee Food")

