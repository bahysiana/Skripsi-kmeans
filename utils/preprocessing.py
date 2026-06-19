import pandas as pd
from sklearn.preprocessing import StandardScaler


# =====================================================
# MEMBERSIHKAN NILAI NUMERIK
# =====================================================

def clean_minutes(value):
    """
    Mengubah:
    '13 menit' -> 13
    '8 menit' -> 8
    15 -> 15
    """

    if pd.isna(value):
        return 0

    text = str(value).lower()

    text = text.replace("menit", "")

    text = text.strip()

    try:
        return float(text)
    except:
        return 0.0


# =====================================================
# PREPROCESSING
# =====================================================

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

    # Pastikan numerik
    numeric_columns = [

        "Total_harga",

        "Jumlah_pesanan",

        "rata_rata_harga",

        "waktu_persiapan_yang_diberikan",

        "waktu_persiapan_digunakan"

    ]

    for col in numeric_columns:

        data[col] = pd.to_numeric(
            data[col],
            errors="coerce"
        )

        data[col] = data[col].fillna(0)

    scaler = StandardScaler()

    scaled = scaler.fit_transform(

        data[numeric_columns]

    )

    scaled_df = pd.DataFrame(

        scaled,

        columns=numeric_columns

    )

    return scaled_df, scaler

