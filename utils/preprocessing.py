import pandas as pd
from sklearn.preprocessing import StandardScaler

# ==========================================================
# FITUR YANG DIGUNAKAN UNTUK K-MEANS
# ==========================================================

FEATURE_COLUMNS = [
    "Total_harga",
    "Jumlah_pesanan",
    "rata_rata_harga",
    "waktu_persiapan_yang_diberikan",
    "waktu_persiapan_digunakan"
]


# ==========================================================
# MEMBERSIHKAN NILAI MENIT
# ==========================================================

def clean_minutes(value):

    if pd.isna(value):
        return 0.0

    value = str(value).lower()
    value = value.replace("menit", "")
    value = value.strip()

    try:
        return float(value)
    except Exception:
        return 0.0


# ==========================================================
# MEMBERSIHKAN DATASET
# ==========================================================

def clean_dataframe(df: pd.DataFrame):

    data = df.copy()

    if "waktu_persiapan_yang_diberikan" in data.columns:

        data["waktu_persiapan_yang_diberikan"] = (
            data["waktu_persiapan_yang_diberikan"]
            .apply(clean_minutes)
        )

    if "waktu_persiapan_digunakan" in data.columns:

        data["waktu_persiapan_digunakan"] = (
            data["waktu_persiapan_digunakan"]
            .apply(clean_minutes)
        )

    numeric_columns = [
        "Total_harga",
        "harga_per_menu",
        "Jumlah_pesanan",
        "rata_rata_harga",
        "waktu_persiapan_yang_diberikan",
        "waktu_persiapan_digunakan"
    ]

    for col in numeric_columns:

        if col in data.columns:

            data[col] = pd.to_numeric(
                data[col],
                errors="coerce"
            )

            data[col] = data[col].fillna(0)

    return data


# ==========================================================
# STANDARD SCALER
# ==========================================================

def preprocess_data(df: pd.DataFrame):

    data = clean_dataframe(df)

    scaler = StandardScaler()

    scaled = scaler.fit_transform(
        data[FEATURE_COLUMNS]
    )

    scaled_df = pd.DataFrame(
        scaled,
        columns=FEATURE_COLUMNS
    )

    return scaled_df, scaler


# ==========================================================
# MENGAMBIL FITUR
# ==========================================================

def get_feature_columns():

    return FEATURE_COLUMNS


# ==========================================================
# MENGAMBIL DATA BERSIH
# ==========================================================

def get_clean_data(df: pd.DataFrame):

    return clean_dataframe(df)
