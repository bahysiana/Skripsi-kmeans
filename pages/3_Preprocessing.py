import streamlit as st
import pandas as pd

from utils.database import get_all_data
from utils.preprocessing import preprocess_data

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Preprocessing",
    page_icon="🧹",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("🧹 Preprocessing Data")

st.caption(
    "Melakukan preprocessing menggunakan StandardScaler sebelum proses K-Means Clustering."
)

st.divider()

# =====================================================
# LOAD DATA
# =====================================================

df = get_all_data()

if df.empty:

    st.warning(
        "Database masih kosong. Silakan tambahkan data terlebih dahulu pada menu Kelola Data."
    )

    st.stop()

# =====================================================
# DATA ASLI
# =====================================================

st.subheader("📋 Data Sebelum Preprocessing")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================================
# TOMBOL PREPROCESSING
# =====================================================

if st.button(
    "🚀 Jalankan Preprocessing",
    use_container_width=True
):

    hasil_scaled, scaler = preprocess_data(df)

    st.session_state["scaled_data"] = hasil_scaled
    st.session_state["original_data"] = df

    st.success(
        "✅ Preprocessing berhasil dilakukan."
    )

# =====================================================
# HASIL
# =====================================================

if "scaled_data" in st.session_state:

    st.subheader("📊 Hasil StandardScaler")

    st.dataframe(
        st.session_state["scaled_data"],
        use_container_width=True,
        hide_index=True
    )

    csv = (
        st.session_state["scaled_data"]
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        label="📥 Download Hasil Preprocessing",
        data=csv,
        file_name="hasil_preprocessing.csv",
        mime="text/csv",
        use_container_width=True
    )
