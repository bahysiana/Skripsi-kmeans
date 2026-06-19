import pandas as pd
from sklearn.preprocessing import StandardScaler


# ==========================================================
# MEMBERSIHKAN KOLOM MENIT
# ==========================================================

def clean_minutes(value):

    if pd.isna(value):
        return 0

    value = str(value)

    value = value.replace("menit", "")

    value = value.replace("Menit", "")

    value = value.strip()

    try:

        return float(value)

    except:

        return 0


# ==========================================================
# PREPROCESSING DATA
# ==========================================================

def preprocess_data(df):

    data = df.copy()

    # Bersihkan kolom waktu

    data["waktu_persiapan_yang_diberikan"] = (
        data["waktu_persiapan_yang_diberikan"]
        .apply(clean_minutes)
    )

    data["waktu_persiapan_digunakan"] = (
        data["waktu_persiapan_digunakan"]
        .apply(clean_minutes)
    )

    # Kolom numerik yang dipakai K-Means

    fitur = [

        "Total_harga",

        "Jumlah_pesanan",

        "rata_rata_harga",

        "waktu_persiapan_yang_diberikan",

        "waktu_persiapan_digunakan"

    ]

    # Pastikan numerik

    for col in fitur:

        data[col] = pd.to_numeric(

            data[col],

            errors="coerce"

        )

        data[col] = data[col].fillna(0)

    scaler = StandardScaler()

    scaled = scaler.fit_transform(

        data[fitur]

    )

    scaled_df = pd.DataFrame(

        scaled,

        columns=fitur

    )

    return scaled_df, scaler
