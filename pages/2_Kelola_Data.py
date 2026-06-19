import streamlit as st
import pandas as pd

from utils.database import (
    get_all_data,
    count_data,
    import_csv,
    truncate_table,
    insert_data,
    update_data,
    delete_data,
    get_data_by_id
)

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Kelola Data",
    page_icon="📂",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("📂 Kelola Data Transaksi")

st.caption(
    "Tambah, ubah, hapus, dan impor data transaksi Shopee Food."
)

st.divider()

# =====================================================
# STATISTIK
# =====================================================

try:
    total_data = count_data()
except Exception:
    total_data = 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📦 Total Data",
        value=total_data
    )

with col2:
    st.metric(
        label="💾 Database",
        value="SQLite"
    )

with col3:
    st.metric(
        label="🤖 Status",
        value="Aktif"
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

        # Membaca file CSV
        preview = pd.read_csv(uploaded_file)

        st.success("✅ File berhasil dibaca.")

        st.write("### Preview Data")

        st.dataframe(
            preview.head(10),
            use_container_width=True,
            hide_index=True
        )

        col_import1, col_import2 = st.columns(2)

        with col_import1:

            if st.button(
                "➕ Tambahkan ke Database",
                use_container_width=True
            ):

                import_csv(preview)

                st.success(
                    "Data berhasil ditambahkan ke database."
                )

                st.rerun()

        with col_import2:

            if st.button(
                "♻️ Ganti Seluruh Data",
                use_container_width=True
            ):

                truncate_table()

                import_csv(preview)

                st.success(
                    "Database berhasil diperbarui dengan data baru."
                )

                st.rerun()

    except Exception as e:

        st.error(
            f"Gagal membaca file CSV: {e}"
        )

st.divider()
# =====================================================
# TAMBAH DATA MANUAL
# =====================================================

st.subheader("➕ Tambah Data Transaksi")

with st.form("form_tambah_data", clear_on_submit=True):

    col1, col2 = st.columns(2)

    with col1:

        username = st.text_input(
            "Username"
        )

        menu_yang_dibeli = st.text_input(
            "Menu yang Dibeli"
        )

        total_harga = st.number_input(
            "Total Harga",
            min_value=0.0,
            value=0.0,
            step=1000.0
        )

        harga_per_menu = st.text_input(
            "Harga per Menu"
        )

        jumlah_pesanan = st.number_input(
            "Jumlah Pesanan",
            min_value=1,
            value=1,
            step=1
        )

    with col2:

        rata_rata_harga = st.number_input(
            "Rata-rata Harga",
            min_value=0.0,
            value=0.0,
            step=1000.0
        )

        waktu_persiapan_yang_diberikan = st.number_input(
            "Waktu Persiapan yang Diberikan (menit)",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

        waktu_persiapan_digunakan = st.number_input(
            "Waktu Persiapan Digunakan (menit)",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

        waktu_pesan = st.text_input(
            "Waktu Pesan (contoh: 2025/05/10 12:30)"
        )

    simpan = st.form_submit_button(
        "💾 Simpan Data"
    )

if simpan:

    if (
        username.strip() == ""
        or menu_yang_dibeli.strip() == ""
        or waktu_pesan.strip() == ""
    ):

        st.warning(
            "Username, Menu yang Dibeli, dan Waktu Pesan wajib diisi."
        )

    else:

        try:

            insert_data(

                username=username,

                menu_yang_dibeli=menu_yang_dibeli,

                Total_harga=total_harga,

                harga_per_menu=harga_per_menu,

                Jumlah_pesanan=jumlah_pesanan,

                rata_rata_harga=rata_rata_harga,

                waktu_persiapan_yang_diberikan=waktu_persiapan_yang_diberikan,

                waktu_persiapan_digunakan=waktu_persiapan_digunakan,

                waktu_pesan=waktu_pesan

            )

            st.success(
                "✅ Data berhasil ditambahkan."
            )

            st.rerun()

        except Exception as e:

            st.error(
                f"Gagal menyimpan data: {e}"
            )

st.divider()

# =====================================================
# PENCARIAN DATA
# =====================================================

st.subheader("🔍 Pencarian Data")

df = get_all_data()

keyword = st.text_input(
    "Cari berdasarkan Username atau Menu yang Dibeli"
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

st.write(f"**Jumlah data ditemukan:** {len(df)}")

st.divider()

# =====================================================
# TABEL DATA
# =====================================================

st.subheader("📋 Data Transaksi Shopee Food")

if df.empty:

    st.info(
        "Belum ada data yang tersedia."
    )

else:

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# =====================================================
# EDIT DATA
# =====================================================

st.subheader("✏️ Edit Data")

data_edit = get_all_data()

if not data_edit.empty:

    id_edit = st.selectbox(
        "Pilih ID yang akan diedit",
        data_edit["id"].tolist(),
        key="edit_id"
    )

    row = get_data_by_id(id_edit)

    if row is not None:

        with st.form("form_edit"):

            username_edit = st.text_input(
                "Username",
                value=row["username"]
            )

            menu_edit = st.text_input(
                "Menu yang Dibeli",
                value=row["menu_yang_dibeli"]
            )

            total_edit = st.number_input(
                "Total Harga",
                min_value=0.0,
                value=float(row["Total_harga"])
            )

            harga_menu_edit = st.text_input(
                "Harga per Menu",
                value=str(row["harga_per_menu"])
            )

            jumlah_edit = st.number_input(
                "Jumlah Pesanan",
                min_value=1,
                value=int(row["Jumlah_pesanan"])
            )

            rata_edit = st.number_input(
                "Rata-rata Harga",
                min_value=0.0,
                value=float(row["rata_rata_harga"])
            )

            wp_diberikan = st.number_input(
                "Waktu Persiapan yang Diberikan",
                min_value=0.0,
                value=float(row["waktu_persiapan_yang_diberikan"])
            )

            wp_digunakan = st.number_input(
                "Waktu Persiapan Digunakan",
                min_value=0.0,
                value=float(row["waktu_persiapan_digunakan"])
            )

            waktu_edit = st.text_input(
                "Waktu Pesan",
                value=row["waktu_pesan"]
            )

            submit_edit = st.form_submit_button(
                "💾 Simpan Perubahan"
            )

        if submit_edit:

            update_data(

                id_data=id_edit,

                username=username_edit,

                menu_yang_dibeli=menu_edit,

                Total_harga=total_edit,

                harga_per_menu=harga_menu_edit,

                Jumlah_pesanan=jumlah_edit,

                rata_rata_harga=rata_edit,

                waktu_persiapan_yang_diberikan=wp_diberikan,

                waktu_persiapan_digunakan=wp_digunakan,

                waktu_pesan=waktu_edit

            )

            st.success(
                "✅ Data berhasil diperbarui."
            )

            st.rerun()

else:

    st.info(
        "Belum ada data yang dapat diedit."
    )

st.divider()

# =====================================================
# HAPUS DATA
# =====================================================

st.subheader("🗑️ Hapus Data")

data_hapus = get_all_data()

if not data_hapus.empty:

    id_hapus = st.selectbox(
        "Pilih ID yang akan dihapus",
        data_hapus["id"].tolist(),
        key="hapus_id"
    )

    konfirmasi = st.checkbox(
        "Saya yakin ingin menghapus data ini."
    )

    if st.button(
        "🗑️ Hapus Data",
        use_container_width=True
    ):

        if konfirmasi:

            delete_data(id_hapus)

            st.success(
                "✅ Data berhasil dihapus."
            )

            st.rerun()

        else:

            st.warning(
                "Silakan centang konfirmasi terlebih dahulu."
            )

else:

    st.info(
        "Belum ada data yang dapat dihapus."
    )

st.divider()

# =====================================================
# INFORMASI
# =====================================================

st.info(
    """
### 📌 Informasi

Halaman ini mendukung fitur:

- ➕ Tambah data transaksi
- 📤 Import dataset CSV
- 🔍 Pencarian data
- ✏️ Edit data transaksi
- 🗑️ Hapus data transaksi
- 💾 Penyimpanan otomatis ke database SQLite
"""
)

