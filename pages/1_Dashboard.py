import streamlit as st
import plotly.express as px

from utils.database import get_all_data

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Analisis Pola Transaksi Shopee Food")
st.caption(
    "Analisis Menggunakan Metode K-Means Clustering"
)

st.divider()

# ==========================================================
# LOAD DATA
# ==========================================================

df = get_all_data()

if df.empty:

    st.warning(
        "Belum ada data. Silakan import data pada menu Kelola Data."
    )

    st.stop()

# ==========================================================
# METRIC
# ==========================================================

total_transaksi = len(df)

total_omzet = df["Total_harga"].sum()

total_item = df["Jumlah_pesanan"].sum()

rata_harga = df["rata_rata_harga"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Transaksi",
    f"{total_transaksi:,}"
)

col2.metric(
    "Total Omzet",
    f"Rp {total_omzet:,.0f}"
)

col3.metric(
    "Total Item",
    f"{int(total_item):,}"
)

col4.metric(
    "Rata-rata Harga",
    f"Rp {rata_harga:,.0f}"
)

st.divider()

# ==========================================================
# HISTOGRAM TOTAL HARGA
# ==========================================================

fig_total = px.histogram(
    df,
    x="Total_harga",
    nbins=20,
    title="Distribusi Total Harga"
)

st.plotly_chart(
    fig_total,
    use_container_width=True
)

# ==========================================================
# HISTOGRAM JUMLAH PESANAN
# ==========================================================

fig_jumlah = px.histogram(
    df,
    x="Jumlah_pesanan",
    nbins=15,
    title="Distribusi Jumlah Pesanan"
)

st.plotly_chart(
    fig_jumlah,
    use_container_width=True
)

# ==========================================================
# SCATTER PLOT
# ==========================================================

fig_scatter = px.scatter(
    df,
    x="Jumlah_pesanan",
    y="Total_harga",
    hover_data=["username"],
    title="Jumlah Pesanan vs Total Harga"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

# ==========================================================
# PREVIEW DATA
# ==========================================================

st.subheader("Preview Dataset")

st.dataframe(
    df.head(20),
    use_container_width=True,
    hide_index=True
)

