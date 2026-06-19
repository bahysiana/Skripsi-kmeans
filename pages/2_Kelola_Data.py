import streamlit as st
import pandas as pd

from utils.database import (
    get_all_data,
    insert_data,
    update_data,
    delete_data,
    get_data_by_id,
    replace_all_data
)

st.set_page_config(
    page_title="Kelola Data",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Kelola Data Transaksi")

st.markdown("---")

# ==========================================================
# IMPORT DATASET
# ==========================================================

st.subheader("📥 Import Dataset CSV")

uploaded_file = st.file_uploader(
    "Pilih file CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        df_import = pd.read_csv(
            uploaded_file,
            sep=";"
        )

        replace_all_data(df_import)

        st.success("Dataset berhasil diimport.")

        st.rerun()

    except Exception as e:

        st.error(e)

st.markdown("---")

# ==========================================================
# LOAD DATA
# ==========================================================

df = get_all_data()

# ==========================================================
# SEARCH
# ==========================================================

st.subheader("🔎 Pencarian")

keyword = st.text_input(
    "Cari Username / Menu"
)

if keyword:

    keyword = keyword.lower()

    df = df[
        (
            df["username"]
            .astype(str)
            .str.lower()
            .str.contains(keyword)
        )
        |
        (
            df["menu_yang_dibeli"]
            .astype(str)
            .str.lower()
            .str.contains(keyword)
        )
    ]

# ==========================================================
# DATAFRAME
# ==========================================================

st.subheader("📋 Dataset")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================================
# FORM TAMBAH DATA
# ==========================================================

st.subheader("➕ Tambah Data")

with st.expander("Buka Form Tambah Data"):

    with st.form("form_tambah"):

        col1, col2 = st.columns(2)

        with col1:

            no = st.number_input(
                "No",
                min_value=1,
                step=1
            )

            username = st.text_input(
                "Username"
            )

            menu = st.text_area(
                "Menu Yang Dibeli"
            )

            total = st.number_input(
                "Total Harga",
                min_value=0.0
            )

            harga = st.number_input(
                "Harga Per Menu",
                min_value=0.0
            )

        with col2:

            jumlah = st.number_input(
                "Jumlah Pesanan",
                min_value=1
            )

            rata = st.number_input(
                "Rata-rata Harga",
                min_value=0.0
            )

            prep1 = st.number_input(
                "Waktu Persiapan Diberikan",
                min_value=0.0
            )

            prep2 = st.number_input(
                "Waktu Persiapan Digunakan",
                min_value=0.0
            )

            waktu = st.text_input(
                "Waktu Pesan"
            )

        simpan = st.form_submit_button(
            "💾 Simpan Data"
        )

        if simpan:

            insert_data(
                no,
                username,
                menu,
                total,
                harga,
                jumlah,
                rata,
                prep1,
                prep2,
                waktu
            )

            st.success(
                "Data berhasil ditambahkan."
            )

            st.rerun()

# ==========================================================
# HAPUS DATA
# ==========================================================

if not df.empty:

    st.markdown("---")

    st.subheader("🗑️ Hapus Data")

    selected_id = st.selectbox(
        "Pilih ID",
        df["id"].tolist()
    )

    if st.button(
        "Hapus Data"
    ):

        delete_data(selected_id)

        st.success(
            "Data berhasil dihapus."
        )

        st.rerun()

