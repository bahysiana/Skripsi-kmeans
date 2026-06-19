import streamlit as st
import pandas as pd

from utils.database import (
    get_all_data,
    insert_data,
    import_csv,
    count_data
)

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Kelola Data",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Kelola Data Transaksi Shopee Food")
st.caption("Tambah data, import CSV, dan kelola dataset penelitian.")

st.divider()

# =====================================================
# RINGKASAN
# =====================================================

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Data",
        count_data()
    )

with col2:
    st.metric(
        "Status",
        "Siap Digunakan"
    )

st.divider()

# =====================================================
# IMPORT CSV
# =====================================================

st.subheader("📤 Import Dataset CSV")

uploaded_file = st.file_uploader(
    "Pilih file CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        import_csv(uploaded_file)

        st.success("✅ Dataset berhasil diimport.")

        st.rerun()

    except Exception as e:

        st.error(f"Terjadi kesalahan: {e}")

st.divider()

# =====================================================
# TAMBAH DATA MANUAL
# =====================================================

st.subheader("➕ Tambah Data Manual")

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

        menu = st.text_input(
            "Menu yang Dibeli"
        )

        total = st.number_input(
            "Total Harga",
            min_value=0.0
        )

        harga_menu = st.number_input(
            "Harga per Menu",
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

        prep_diberikan = st.number_input(
            "Waktu Persiapan Diberikan",
            min_value=0.0
        )

        prep_digunakan = st.number_input(
            "Waktu Persiapan Digunakan",
            min_value=0.0
        )

        waktu = st.text_input(
            "Waktu Pesan"
        )

    submit = st.form_submit_button(
        "💾 Simpan Data"
    )

    if submit:

        insert_data(
            no=no,
            username=username,
            menu_yang_dibeli=menu,
            Total_harga=total,
            harga_per_menu=harga_menu,
            Jumlah_pesanan=jumlah,
            rata_rata_harga=rata,
            waktu_persiapan_yang_diberikan=prep_diberikan,
            waktu_persiapan_digunakan=prep_digunakan,
            waktu_pesan=waktu
        )

        st.success("✅ Data berhasil ditambahkan.")

        st.rerun()

# =====================================================
# TAMPILKAN DATA
# =====================================================

st.divider()
st.subheader("📊 Data Transaksi")

df = get_all_data()

if not df.empty:

    keyword = st.text_input(
        "🔍 Cari Username / Menu",
        placeholder="Masukkan kata kunci..."
    )

    if keyword:

        keyword = keyword.lower()

        df = df[
            (
                df["username"]
                .astype(str)
                .str.lower()
                .str.contains(keyword, na=False)
            )
            |
            (
                df["menu_yang_dibeli"]
                .astype(str)
                .str.lower()
                .str.contains(keyword, na=False)
            )
        ]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("Belum ada data pada database.")

# =====================================================
# HAPUS DATA
# =====================================================

st.divider()
st.subheader("🗑️ Hapus Data")

if not df.empty:

    id_hapus = st.selectbox(
        "Pilih ID yang akan dihapus",
        df["id"].tolist()
    )

    if st.button(
        "Hapus Data",
        type="primary"
    ):

        from utils.database import delete_data

        delete_data(id_hapus)

        st.success("✅ Data berhasil dihapus.")

        st.rerun()

# =====================================================
# EDIT DATA
# =====================================================

st.divider()
st.subheader("✏️ Edit Data")

if not df.empty:

    id_edit = st.selectbox(
        "Pilih ID yang akan diedit",
        df["id"].tolist(),
        key="edit_data"
    )

    from utils.database import (
        get_data_by_id,
        update_data
    )

    row = get_data_by_id(id_edit)

    if row:

        with st.form("form_edit"):

            no = st.number_input(
                "No",
                value=int(row["no"])
            )

            username = st.text_input(
                "Username",
                value=row["username"]
            )

            menu = st.text_input(
                "Menu yang Dibeli",
                value=row["menu_yang_dibeli"]
            )

            total = st.number_input(
                "Total Harga",
                value=float(row["Total_harga"])
            )

            harga = st.number_input(
                "Harga per Menu",
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
                value=float(row["waktu_persiapan_yang_diberikan"])
            )

            prep2 = st.number_input(
                "Waktu Persiapan Digunakan",
                value=float(row["waktu_persiapan_digunakan"])
            )

            waktu = st.text_input(
                "Waktu Pesan",
                value=row["waktu_pesan"]
            )

            simpan = st.form_submit_button(
                "💾 Simpan Perubahan"
            )

            if simpan:

                update_data(
                    id_value=id_edit,
                    no=no,
                    username=username,
                    menu_yang_dibeli=menu,
                    Total_harga=total,
                    harga_per_menu=harga,
                    Jumlah_pesanan=jumlah,
                    rata_rata_harga=rata,
                    waktu_persiapan_yang_diberikan=prep1,
                    waktu_persiapan_digunakan=prep2,
                    waktu_pesan=waktu
                )

                st.success("✅ Data berhasil diperbarui.")

                st.rerun()

