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
    page_icon="📋",
    layout="wide"
)

st.title("📋 Kelola Data")

# ==========================================================
# IMPORT CSV
# ==========================================================

st.subheader("Import Dataset")

uploaded_file = st.file_uploader(
    "Upload File CSV",
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

st.divider()

# ==========================================================
# TAMPILKAN DATA
# ==========================================================

df = get_all_data()

st.subheader("Data Transaksi")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# TAMBAH DATA
# ==========================================================

st.subheader("Tambah Data")

with st.form("form_tambah"):

    no = st.number_input("No", 1, step=1)

    username = st.text_input("Username")

    menu = st.text_input("Menu Yang Dibeli")

    total = st.number_input("Total Harga", 0.0)

    harga_menu = st.number_input("Harga Per Menu", 0.0)

    jumlah = st.number_input("Jumlah Pesanan", 1)

    rata = st.number_input("Rata-rata Harga", 0.0)

    prep1 = st.number_input(
        "Waktu Persiapan Diberikan",
        0.0
    )

    prep2 = st.number_input(
        "Waktu Persiapan Digunakan",
        0.0
    )

    waktu = st.text_input(
        "Waktu Pesan"
    )

    submit = st.form_submit_button(
        "Simpan"
    )

    if submit:

        insert_data(
            no,
            username,
            menu,
            total,
            harga_menu,
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

st.divider()

# ==========================================================
# EDIT DATA
# ==========================================================

if not df.empty:

    st.subheader("Edit Data")

    id_edit = st.selectbox(
        "Pilih ID",
        df["id"]
    )

    row = get_data_by_id(id_edit)

    with st.form("edit_form"):

        no = st.number_input(
            "No",
            value=int(row["no"])
        )

        username = st.text_input(
            "Username",
            value=row["username"]
        )

        menu = st.text_input(
            "Menu Yang Dibeli",
            value=row["menu_yang_dibeli"]
        )

        total = st.number_input(
            "Total Harga",
            value=float(row["Total_harga"])
        )

        harga = st.number_input(
            "Harga Per Menu",
            value=float(row["harga_per_menu"])
        )

        jumlah = st.number_input(
            "Jumlah Pesanan",
            value=int(row["Jumlah_pesanan"])
        )

        rata = st.number_input(
            "Rata-rata Harga",
            value=float(row["rata_rata_harga"])
        )

        prep1 = st.number_input(
            "Waktu Persiapan Diberikan",
            value=float(
                row["waktu_persiapan_yang_diberikan"]
            )
        )

        prep2 = st.number_input(
            "Waktu Persiapan Digunakan",
            value=float(
                row["waktu_persiapan_digunakan"]
            )
        )

        waktu = st.text_input(
            "Waktu Pesan",
            value=row["waktu_pesan"]
        )

        simpan = st.form_submit_button(
            "Update"
        )

        if simpan:

            update_data(
                id_edit,
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
                "Data berhasil diperbarui."
            )

            st.rerun()

st.divider()

# ==========================================================
# HAPUS DATA
# ==========================================================

if not df.empty:

    st.subheader("Hapus Data")

    id_hapus = st.selectbox(
        "Pilih ID Yang Akan Dihapus",
        df["id"],
        key="hapus"
    )

    if st.button(
        "Hapus Data"
    ):

        delete_data(id_hapus)

        st.success(
            "Data berhasil dihapus."
        )

        st.rerun()

