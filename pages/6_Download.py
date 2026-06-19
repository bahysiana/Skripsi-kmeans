import streamlit as st

st.set_page_config(
    page_title="Download",
    page_icon="📥",
    layout="wide"
)

st.title("📥 Download Hasil")

# ==========================================================
# HASIL CLUSTERING
# ==========================================================

if "hasil_cluster" not in st.session_state:

    st.warning(
        "Belum ada hasil clustering yang dapat diunduh."
    )

    st.stop()

hasil = st.session_state["hasil_cluster"]

csv_hasil = hasil.to_csv(
    index=False
).encode("utf-8")

st.subheader("Download Dataset Hasil Clustering")

st.download_button(
    label="📄 Download CSV Hasil Clustering",
    data=csv_hasil,
    file_name="hasil_clustering.csv",
    mime="text/csv",
    use_container_width=True
)

# ==========================================================
# HASIL PREPROCESSING
# ==========================================================

if "scaled_df" in st.session_state:

    scaled = st.session_state["scaled_df"]

    csv_scaled = scaled.to_csv(
        index=False
    ).encode("utf-8")

    st.subheader("Download Hasil Preprocessing")

    st.download_button(
        label="📄 Download CSV Preprocessing",
        data=csv_scaled,
        file_name="hasil_preprocessing.csv",
        mime="text/csv",
        use_container_width=True
    )

# ==========================================================
# CENTROID
# ==========================================================

if "centroid" in st.session_state:

    centroid = st.session_state["centroid"]

    csv_centroid = centroid.to_csv(
        index=False
    ).encode("utf-8")

    st.subheader("Download Data Centroid")

    st.download_button(
        label="📄 Download CSV Centroid",
        data=csv_centroid,
        file_name="centroid.csv",
        mime="text/csv",
        use_container_width=True
    )

# ==========================================================
# STATISTIK CLUSTER
# ==========================================================

if "cluster_statistics" in st.session_state:

    statistik = st.session_state["cluster_statistics"]

    csv_statistik = statistik.to_csv(
        index=False
    ).encode("utf-8")

    st.subheader("Download Statistik Cluster")

    st.download_button(
        label="📄 Download CSV Statistik Cluster",
        data=csv_statistik,
        file_name="statistik_cluster.csv",
        mime="text/csv",
        use_container_width=True
    )

# ==========================================================
# RINGKASAN CLUSTER
# ==========================================================

if "summary_cluster" in st.session_state:

    summary = st.session_state["summary_cluster"]

    csv_summary = summary.to_csv(
        index=False
    ).encode("utf-8")

    st.subheader("Download Ringkasan Cluster")

    st.download_button(
        label="📄 Download CSV Ringkasan Cluster",
        data=csv_summary,
        file_name="ringkasan_cluster.csv",
        mime="text/csv",
        use_container_width=True
    )

