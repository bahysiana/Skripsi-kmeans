import streamlit as st
import plotly.express as px

from utils.clustering import (
    elbow_method,
    run_kmeans,
    calculate_silhouette,
    add_cluster_result,
    add_cluster_label,
    cluster_summary,
    cluster_statistics
)

st.set_page_config(
    page_title="K-Means Clustering",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 K-Means Clustering")

st.markdown("---")

# ==========================================================
# VALIDASI
# ==========================================================

if "scaled_df" not in st.session_state:

    st.warning(
        "Silakan lakukan preprocessing terlebih dahulu."
    )

    st.stop()

scaled_df = st.session_state["scaled_df"]
original_df = st.session_state["original_df"]

# ==========================================================
# ELBOW METHOD
# ==========================================================

st.subheader("📈 Elbow Method")

elbow_df = elbow_method(
    scaled_df,
    max_k=10
)

fig_elbow = px.line(
    elbow_df,
    x="K",
    y="WCSS",
    markers=True,
    title="Elbow Method"
)

st.plotly_chart(
    fig_elbow,
    use_container_width=True
)

st.info(
    "Penelitian ini menggunakan K = 3 sebagai jumlah cluster."
)

st.markdown("---")

# ==========================================================
# PROSES CLUSTERING
# ==========================================================

if st.button(
    "🚀 Jalankan K-Means",
    use_container_width=True
):

    model, labels, centroid = run_kmeans(
        scaled_df
    )

    silhouette = calculate_silhouette(
        scaled_df,
        labels
    )

    hasil = add_cluster_result(
        original_df,
        labels
    )

    hasil = add_cluster_label(
        hasil
    )

    summary = cluster_summary(
        hasil
    )

    statistik = cluster_statistics(
        hasil
    )

    st.session_state["hasil_cluster"] = hasil
    st.session_state["centroid"] = centroid
    st.session_state["summary_cluster"] = summary
    st.session_state["cluster_statistics"] = statistik
    st.session_state["silhouette"] = silhouette

# ==========================================================
# TAMPILKAN HASIL
# ==========================================================

if "hasil_cluster" in st.session_state:

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Jumlah Cluster",
            "3"
        )

    with col2:

        st.metric(
            "Silhouette Score",
            round(
                st.session_state["silhouette"],
                4
            )
        )

    st.markdown("---")

    st.subheader("📍 Centroid")

    st.dataframe(
        st.session_state["centroid"],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("📊 Statistik Cluster")

    st.dataframe(
        st.session_state["cluster_statistics"],
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("🥧 Distribusi Cluster")

    fig_pie = px.pie(
        st.session_state["summary_cluster"],
        names="cluster",
        values="Jumlah Data",
        hole=0.45
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("📋 Hasil Clustering")

    st.dataframe(
        st.session_state["hasil_cluster"],
        use_container_width=True,
        hide_index=True
    )

    csv = (
        st.session_state["hasil_cluster"]
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        label="⬇️ Download Hasil Clustering",
        data=csv,
        file_name="hasil_kmeans.csv",
        mime="text/csv",
        use_container_width=True
    )

