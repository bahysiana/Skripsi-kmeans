import sqlite3
from pathlib import Path
import pandas as pd

# ==========================================================
# KONFIGURASI DATABASE
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "database"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "shopee_food.db"


# ==========================================================
# KONEKSI DATABASE
# ==========================================================

def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ==========================================================
# MEMBUAT TABEL
# ==========================================================

def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaksi (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            no INTEGER,

            username TEXT,

            menu_yang_dibeli TEXT,

            Total_harga REAL,

            harga_per_menu REAL,

            Jumlah_pesanan INTEGER,

            rata_rata_harga REAL,

            waktu_persiapan_yang_diberikan REAL,

            waktu_persiapan_digunakan REAL,

            waktu_pesan TEXT

        )
    """)

    conn.commit()
    conn.close()


# ==========================================================
# AMBIL SEMUA DATA
# ==========================================================

def get_all_data():

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM transaksi
        ORDER BY no ASC
        """,
        conn
    )

    conn.close()

    return df


# ==========================================================
# HITUNG JUMLAH DATA
# ==========================================================

def count_data():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM transaksi
        """
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ==========================================================
# AMBIL DATA BERDASARKAN ID
# ==========================================================

def get_data_by_id(id_value):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM transaksi
        WHERE id = ?
        """,
        (id_value,)
    )

    row = cursor.fetchone()

    conn.close()

    return row


# ==========================================================
# TAMBAH DATA
# ==========================================================

def insert_data(
    no,
    username,
    menu_yang_dibeli,
    Total_harga,
    harga_per_menu,
    Jumlah_pesanan,
    rata_rata_harga,
    waktu_persiapan_yang_diberikan,
    waktu_persiapan_digunakan,
    waktu_pesan
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO transaksi
        (
            no,
            username,
            menu_yang_dibeli,
            Total_harga,
            harga_per_menu,
            Jumlah_pesanan,
            rata_rata_harga,
            waktu_persiapan_yang_diberikan,
            waktu_persiapan_digunakan,
            waktu_pesan
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            no,
            username,
            menu_yang_dibeli,
            Total_harga,
            harga_per_menu,
            Jumlah_pesanan,
            rata_rata_harga,
            waktu_persiapan_yang_diberikan,
            waktu_persiapan_digunakan,
            waktu_pesan
        )
    )

    conn.commit()
    conn.close()


# ==========================================================
# HAPUS SEMUA DATA
# ==========================================================

def truncate_table():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM transaksi"
    )

    conn.commit()

    conn.close()


# ==========================================================
# IMPORT DATAFRAME
# ==========================================================

def import_dataframe(df):

    conn = get_connection()

    if "id" in df.columns:
        df = df.drop(columns=["id"])

    # Bersihkan kolom waktu persiapan
    for col in [
        "waktu_persiapan_yang_diberikan",
        "waktu_persiapan_digunakan"
    ]:

        if col in df.columns:

            df[col] = (
                df[col]
                .astype(str)
                .str.replace(" menit", "", regex=False)
                .str.strip()
            )

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            ).fillna(0)

    df.to_sql(
        "transaksi",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()


# ==========================================================
# INISIALISASI
# ==========================================================

create_table()

# ==========================================================
# UPDATE DATA
# ==========================================================

def update_data(
    id_value,
    no,
    username,
    menu_yang_dibeli,
    Total_harga,
    harga_per_menu,
    Jumlah_pesanan,
    rata_rata_harga,
    waktu_persiapan_yang_diberikan,
    waktu_persiapan_digunakan,
    waktu_pesan
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE transaksi
        SET
            no = ?,
            username = ?,
            menu_yang_dibeli = ?,
            Total_harga = ?,
            harga_per_menu = ?,
            Jumlah_pesanan = ?,
            rata_rata_harga = ?,
            waktu_persiapan_yang_diberikan = ?,
            waktu_persiapan_digunakan = ?,
            waktu_pesan = ?
        WHERE id = ?
        """,
        (
            no,
            username,
            menu_yang_dibeli,
            Total_harga,
            harga_per_menu,
            Jumlah_pesanan,
            rata_rata_harga,
            waktu_persiapan_yang_diberikan,
            waktu_persiapan_digunakan,
            waktu_pesan,
            id_value
        )
    )

    conn.commit()
    conn.close()


# ==========================================================
# HAPUS DATA
# ==========================================================

def delete_data(id_value):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM transaksi
        WHERE id = ?
        """,
        (id_value,)
    )

    conn.commit()
    conn.close()


# ==========================================================
# IMPORT CSV
# ==========================================================

def import_csv(uploaded_file, separator=";"):

    df = pd.read_csv(
        uploaded_file,
        sep=separator
    )

    import_dataframe(df)

    return df


# ==========================================================
# GANTI SELURUH DATA
# ==========================================================

def replace_all_data(df):

    truncate_table()
    import_dataframe(df)


# ==========================================================
# EXPORT DATA
# ==========================================================

def export_dataframe():

    return get_all_data()


# ==========================================================
# INISIALISASI DATABASE
# ==========================================================

create_table()

