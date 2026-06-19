import pandas as pd
from sklearn.preprocessing import StandardScaler


# =====================================================
# MEMBERSIHKAN NILAI NUMERIK
# =====================================================

def clean_numeric(value):
    """
    Mengubah nilai seperti:
    - '13 menit' -> 13
    - '20.000' -> 20000
    - None -> 0
    """

    if pd.isna(value):
        return 0

    value = str(value)

    value = value.replace("menit", "")
    value = value.replace(".", "")
    value = value.replace(",", "")
    value = value.strip()

    try:
        return float(value)
    except:
        return 0


# =====================================================
# PREPROCESSING DATA
# =====================================================

def preprocess_data(df):
    """
    Membersihkan data dan melakukan StandardScaler.
    """

    data = df.copy()

    # Membersihkan kolom numerik
    data["Total_harga"] = data["Total_harga"].apply(clean_numeric)
    data["Jumlah_pesanan"] = data["Jumlah_pesanan"].apply(clean_numeric)
    data["rata_rata_harga"] = data["rata_rata_harga"].apply(clean_numeric)
    data["waktu_persiapan_yang_diberikan"] = (
        data["waktu_persiapan_yang_diberikan"].apply(clean_numeric)
    )
    data["waktu_persiapan_digunakan"] = (
        data["waktu_persiapan_digunakan"].apply(clean_numeric)
    )

    # Fitur yang digunakan untuk clustering
    fitur = [
        "Total_harga",
        "Jumlah_pesanan",
        "rata_rata_harga",
        "waktu_persiapan_yang_diberikan",
        "waktu_persiapan_digunakan",
    ]

    scaler = StandardScaler()

    data_scaled = scaler.fit_transform(data[fitur])

    hasil = pd.DataFrame(
        data_scaled,
        columns=fitur
    )

    return hasil, scaler
