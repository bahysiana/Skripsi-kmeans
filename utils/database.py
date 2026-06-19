import sqlite3
from pathlib import Path
import pandas as pd

# =====================================================
# KONFIGURASI DATABASE
# =====================================================

# Membuat folder database jika belum ada
DATABASE_DIR = Path("database")
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

# Lokasi file SQLite
DB_PATH = DATABASE_DIR / "shopee_food.db"


# =====================================================
# MEMBUAT KONEKSI DATABASE
# =====================================================

def get_connection():
    """
    Membuat koneksi ke database SQLite.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# =====================================================
# MEMBUAT TABEL TRANSAKSI
# =====================================================

def create_table():
    """
    Membuat tabel transaksi jika belum tersedia.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaksi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT NOT NULL,

            menu_yang_dibeli TEXT NOT NULL,

            Total_harga REAL NOT NULL,

            harga_per_menu TEXT NOT NULL,

            Jumlah_pesanan INTEGER NOT NULL,

            rata_rata_harga REAL NOT NULL,

            waktu_persiapan_yang_diberikan REAL NOT NULL,

            waktu_persiapan_digunakan REAL NOT NULL,

            waktu_pesan TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# =====================================================
# INISIALISASI DATABASE
# =====================================================

create_table()
# =====================================================
# AMBIL SEMUA DATA
# =====================================================

def get_all_data():
    """
    Mengambil seluruh data dari tabel transaksi.
    """
    conn = get_connection()

    try:
        df = pd.read_sql_query(
            """
            SELECT *
            FROM transaksi
            ORDER BY id ASC
            """,
            conn
        )

    except Exception:
        df = pd.DataFrame(
            columns=[
                "id",
                "username",
                "menu_yang_dibeli",
                "Total_harga",
                "harga_per_menu",
                "Jumlah_pesanan",
                "rata_rata_harga",
                "waktu_persiapan_yang_diberikan",
                "waktu_persiapan_digunakan",
                "waktu_pesan"
            ]
        )

    conn.close()
    return df


# =====================================================
# AMBIL DATA BERDASARKAN ID
# =====================================================

def get_data_by_id(id_data):
    """
    Mengambil satu data berdasarkan ID.
    """
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM transaksi
        WHERE id = ?
        """,
        (id_data,)
    )

    row = cursor.fetchone()

    conn.close()

    return row


# =====================================================
# HITUNG JUMLAH DATA
# =====================================================

def count_data():
    """
    Menghitung jumlah seluruh transaksi.
    """
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


# =====================================================
# TAMBAH DATA
# =====================================================

def insert_data(
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
    """
    Menambahkan satu data transaksi.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO transaksi
        (
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

        VALUES
        (
            ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        """,

        (
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
# =====================================================
# UPDATE DATA
# =====================================================

def update_data(
    id_data,
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
    """
    Mengubah data transaksi berdasarkan ID.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE transaksi
        SET
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
            username,
            menu_yang_dibeli,
            Total_harga,
            harga_per_menu,
            Jumlah_pesanan,
            rata_rata_harga,
            waktu_persiapan_yang_diberikan,
            waktu_persiapan_digunakan,
            waktu_pesan,
            id_data
        )
    )

    conn.commit()
    conn.close()


# =====================================================
# HAPUS DATA
# =====================================================

def delete_data(id_data):
    """
    Menghapus data berdasarkan ID.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM transaksi
        WHERE id = ?
        """,
        (id_data,)
    )

    conn.commit()
    conn.close()


# =====================================================
# IMPORT DATAFRAME / CSV
# =====================================================

def import_csv(df):
    """
    Mengimpor DataFrame ke database.
    """

    conn = get_connection()

    df.to_sql(
        "transaksi",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()


# =====================================================
# HAPUS SEMUA DATA
# =====================================================

def truncate_table():
    """
    Menghapus seluruh isi tabel transaksi.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM transaksi
        """
    )

    conn.commit()
    conn.close()


# =====================================================
# EXPORT DATAFRAME
# =====================================================

def export_dataframe():
    """
    Mengembalikan seluruh data dalam bentuk DataFrame.
    """

    return get_all_data()


# =====================================================
# GANTI SELURUH DATA
# =====================================================

def replace_all_data(df):
    """
    Menghapus data lama lalu menggantinya dengan data baru.
    """

    truncate_table()
    import_csv(df)


# =====================================================
# SIMPAN DATAFRAME
# =====================================================

def save_dataframe(df):
    """
    Menyimpan DataFrame ke database.
    """

    replace_all_data(df)
