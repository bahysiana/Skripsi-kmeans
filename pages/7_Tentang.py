import streamlit as st

st.set_page_config(
    page_title="Tentang",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ Tentang Aplikasi")

st.markdown("---")

st.markdown(
    """
    ## 🍽️ Analisis Pola Transaksi Shopee Food

    Aplikasi ini dikembangkan untuk membantu melakukan analisis
    pola transaksi menggunakan algoritma **K-Means Clustering**
    berdasarkan data pemesanan pada **Buffet The Padang Pasir**.

    Sistem dibangun menggunakan **Python**, **Streamlit**,
    **SQLite**, dan **Scikit-Learn**.
    """
)

st.markdown("---")

st.subheader("🎯 Tujuan")

st.write("""
Mengelompokkan pola transaksi pelanggan sehingga dapat membantu
pemilik usaha dalam memahami karakteristik pemesanan dan
mendukung pengambilan keputusan berbasis data.
""")

st.markdown("---")

st.subheader("⚙️ Teknologi")

col1, col2 = st.columns(2)

with col1:

    st.success("🐍 Python")

    st.success("📊 Streamlit")

    st.success("🗄️ SQLite")

with col2:

    st.success("🤖 Scikit-Learn")

    st.success("📈 Plotly")

    st.success("🐼 Pandas")

st.markdown("---")

st.subheader("🧠 Metode")

st.markdown("""
- Data Cleaning
- StandardScaler
- Elbow Method
- Silhouette Score
- K-Means Clustering (K = 3)
""")

st.markdown("---")

st.subheader("📌 Variabel yang Digunakan")

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

st.subheader("👨‍🎓 Informasi Penelitian")

st.info("""
Analisis Pola Transaksi Shopee Food
Menggunakan Metode K-Means Clustering
Berdasarkan Data Pemesanan
Pada Toko Buffet The Padang Pasir.
""")

st.markdown("---")

st.caption("© 2026 | Sistem Analisis K-Means Clustering")

