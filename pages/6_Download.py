import streamlit as st

st.set_page_config(
    page_title="Download",
    page_icon="⬇️",
    layout="wide"
)

st.title("⬇️ Download Hasil")

st.markdown("---")

# ==========================================================
# VALIDASI
# ==========================================================

if "hasil_cluster" not in st.session_state:

    st.warning(
        "Belum ada hasil clustering yang dapat diunduh."
    )

    st.stop()

# ==========================================================
# DATA
# ==========================================================

hasil = st.session_state["hasil_cluster"]

scaled = st.session_state.get("scaled_df", None)

centroid = st.session_state.get("centroid", None)

summary = st.session_state.get("summary_cluster", None)

statistik = st.session_state.get("cluster_statistics", None)

# ==========================================================
# HASIL CLUSTERING
# ==========================================================

st.subheader("📄 Dataset Hasil Clustering")

csv_hasil = hasil.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Hasil Clustering",
    data=csv_hasil,
    file_name="hasil_clustering.csv",
    mime="text/csv",
    use_container_width=True
)

# ==========================================================
# HASIL PREPROCESSING
# ==========================================================

if scaled is not None:

    st.subheader("🧹 Hasil Preprocessing")

    csv_scaled = scaled.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Hasil Preprocessing",
        data=csv_scaled,
        file_name="hasil_preprocessing.csv",
        mime="text/csv",
        use_container_width=True
    )

# ==========================================================
# CENTROID
# ==========================================================

if centroid is not None:

    st.subheader("📍 Data Centroid")

    csv_centroid = centroid.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Centroid",
        data=csv_centroid,
        file_name="centroid.csv",
        mime="text/csv",
        use_container_width=True
    )

# ==========================================================
# RINGKASAN CLUSTER
# ==========================================================

if summary is not None:

    st.subheader("📊 Ringkasan Cluster")

    csv_summary = summary.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Ringkasan Cluster",
        data=csv_summary,
        file_name="ringkasan_cluster.csv",
        mime="text/csv",
        use_container_width=True
    )

# ==========================================================
# STATISTIK CLUSTER
# ==========================================================

if statistik is not None:

    st.subheader("📈 Statistik Cluster")

    csv_stat = statistik.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Statistik Cluster",
        data=csv_stat,
        file_name="statistik_cluster.csv",
        mime="text/csv",
        use_container_width=True
    )

st.markdown("---")

st.success(
    "Seluruh hasil analisis dapat diunduh dalam format CSV."
)
