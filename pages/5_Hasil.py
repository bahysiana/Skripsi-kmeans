import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Hasil Clustering",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Hasil Clustering")

st.markdown("---")

# ==========================================================
# VALIDASI
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
# KPI
# ==========================================================

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Jumlah Cluster",
        "3"
    )

with c2:

    st.metric(
        "Silhouette Score",
        round(silhouette, 4)
    )

with c3:

    st.metric(
        "Jumlah Data",
        len(hasil)
    )

st.markdown("---")

# ==========================================================
# DISTRIBUSI CLUSTER
# ==========================================================

left, right = st.columns(2)

with left:

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

with right:

    fig_bar = px.bar(
        summary,
        x="cluster",
        y="Jumlah Data",
        text="Jumlah Data",
        title="Jumlah Anggota Tiap Cluster"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

st.markdown("---")

# ==========================================================
# VISUALISASI CLUSTER
# ==========================================================

fig_scatter = px.scatter(
    hasil,
    x="Jumlah_pesanan",
    y="Total_harga",
    color="Label",
    hover_name="username",
    size="rata_rata_harga",
    title="Visualisasi Cluster"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# CENTROID
# ==========================================================

st.subheader("📍 Nilai Centroid")

st.dataframe(
    centroid,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================================
# STATISTIK
# ==========================================================

st.subheader("📊 Statistik Cluster")

st.dataframe(
    statistik,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================================
# HASIL AKHIR
# ==========================================================

st.subheader("📄 Dataset Hasil Clustering")

st.dataframe(
    hasil,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================================
# DOWNLOAD
# ==========================================================

csv = hasil.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Hasil Clustering",
    data=csv,
    file_name="hasil_clustering.csv",
    mime="text/csv",
    use_container_width=True
)

