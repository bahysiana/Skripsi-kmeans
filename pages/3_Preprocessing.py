import streamlit as st
import pandas as pd

from utils.database import get_all_data
from utils.preprocessing import (
    clean_dataframe,
    preprocess_data,
    get_feature_columns
)

st.set_page_config(
    page_title="Preprocessing",
    page_icon="🧹",
    layout="wide"
)

st.title("🧹 Preprocessing Data")

# ==========================================================
# LOAD DATA
# ==========================================================

df = get_all_data()

if df.empty:

    st.warning(
        "Database masih kosong."
    )

    st.stop()

# ==========================================================
# DATA ASLI
# ==========================================================

st.subheader("Dataset Asli")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# CLEANING
# ==========================================================

clean_df = clean_dataframe(df)

st.subheader("Dataset Setelah Cleaning")

st.dataframe(
    clean_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# FITUR YANG DIGUNAKAN
# ==========================================================

fitur = get_feature_columns()

st.subheader("Fitur Clustering")

st.write(fitur)

st.divider()

# ==========================================================
# STANDARD SCALER
# ==========================================================

scaled_df, scaler = preprocess_data(df)

st.subheader("Hasil StandardScaler")

st.dataframe(
    scaled_df,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# SIMPAN KE SESSION
# ==========================================================

st.session_state["original_df"] = clean_df

st.session_state["scaled_df"] = scaled_df

st.session_state["scaler"] = scaler

st.success(
    "Preprocessing berhasil dilakukan."
)

st.divider()

# ==========================================================
# DOWNLOAD
# ==========================================================

csv = scaled_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Hasil Preprocessing",
    data=csv,
    file_name="hasil_preprocessing.csv",
    mime="text/csv"
)

