```python
import streamlit as st
import plotly.express as px

from utils.clustering import (
    elbow_method,
    run_kmeans,
    calculate_silhouette,
    add_cluster_result,
    add_interpretation,
    cluster_summary
)

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="K-Means Clustering",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 K-Means Clustering")

st.caption(
    "Analisis pola transaksi menggunakan Elbow Method, Silhouette Score, dan K-Means Clustering."
)

st.divider()

# =====================================================
# CEK PREPROCESSING
# =====================================================

if "scaled_data" not in st.session_state:

    st.warning(
        "Silakan jalankan preprocessing terlebih dahulu."
    )

    st.stop()

scaled_df = st.session_state["scaled_data"]
original_df = st.session_state["original_data"]

# =====================================================
# ELBOW METHOD
# =====================================================

st.subheader("📈 Elbow Method")

elbow_df = elbow_method(
    scaled_df,
    max_k=10
)

fig = px.line(
    elbow_df,
    x="K",
    y="WCSS",
    markers=True,
    title="Grafik Elbow Method"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.info(
    "Pada penelitian ini dipilih nilai K = 3 berdasarkan hasil analisis Elbow Method."
)

st.divider()

# =====================================================
# PROSES K-MEANS
# =====================================================

if st.button(
    "🚀 Jalankan K-Means (K = 3)",
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

    hasil = add_interpretation(
        hasil
    )

    summary = cluster_summary(
        hasil
    )

    st.session_state["hasil_cluster"] = hasil
    st.session_state["centroid"] = centroid
    st.session_state["summary_cluster"] = summary
    st.session_state["silhouette"] = silhouette

    st.success(
        "✅ Proses clustering berhasil."
    )

# =====================================================
# HASIL
# =====================================================

if "hasil_cluster" in st.session_state:

    st.subheader("📊 Silhouette Score")

    st.metric(
        "Nilai Silhouette Score",
        round(
            st.session_state["silhouette"],
            4
        )
    )

    st.divider()

    st.subheader("📍 Centroid")

    st.dataframe(
        st.session_state["centroid"],
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📋 Hasil Clustering")

    st.dataframe(
        st.session_state["hasil_cluster"],
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("📈 Distribusi Cluster")

    pie = px.pie(
        st.session_state["summary_cluster"],
        names="Interpretasi",
        values="Jumlah Data",
        hole=0.45
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )
```
