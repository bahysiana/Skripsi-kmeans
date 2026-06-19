import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Hasil Clustering",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Hasil Clustering")

# ==========================================================
# CEK HASIL
# ==========================================================

if "hasil_cluster" not in st.session_state:

    st.warning(
        "Silakan jalankan proses K-Means terlebih dahulu."
    )

    st.stop()

hasil = st.session_state["hasil_cluster"]
summary = st.session_state["summary_cluster"]
centroid = st.session_state["centroid"]
statistik = st.session_state["cluster_statistics"]
silhouette = st.session_state["silhouette"]

# ==========================================================
# SILHOUETTE SCORE
# ==========================================================

st.subheader("Silhouette Score")

st.metric(
    label="Nilai Silhouette",
    value=round(silhouette, 4)
)

st.divider()

# ==========================================================
# JUMLAH DATA PER CLUSTER
# ==========================================================

st.subheader("Jumlah Data Setiap Cluster")

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# PIE CHART
# ==========================================================

fig_pie = px.pie(
    summary,
    names="cluster",
    values="Jumlah Data",
    hole=0.45,
    title="Distribusi Cluster"
)

st.plotly_chart(
    fig_pie,
    use_container_width=True
)

st.divider()

# ==========================================================
# CENTROID
# ==========================================================

st.subheader("Nilai Centroid")

st.dataframe(
    centroid,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# STATISTIK CLUSTER
# ==========================================================

st.subheader("Rata-rata Tiap Cluster")

st.dataframe(
    statistik,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# HASIL AKHIR
# ==========================================================

st.subheader("Dataset Hasil Clustering")

st.dataframe(
    hasil,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# SCATTER PLOT
# ==========================================================

fig_scatter = px.scatter(
    hasil,
    x="Jumlah_pesanan",
    y="Total_harga",
    color="Label",
    hover_data=["username"],
    title="Visualisasi Hasil Clustering"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

st.divider()

# ==========================================================
# DOWNLOAD
# ==========================================================

csv = hasil.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Hasil Clustering",
    data=csv,
    file_name="hasil_clustering.csv",
    mime="text/csv",
    use_container_width=True
)

