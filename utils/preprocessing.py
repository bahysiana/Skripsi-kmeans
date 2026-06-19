import pandas as pd
from sklearn.preprocessing import StandardScaler

# ==========================================================
# MEMBERSIHKAN NILAI MENIT
# ==========================================================

def clean_minutes(value):
    """
    Mengubah:
    '15 menit' -> 15
    '8 Menit'  -> 8
    10         -> 10
    """

    if pd.isna(value):
        return 0.0

    text = str(value).lower()
    text = text.replace("menit", "")
    text = text.strip()

    try:
        return float(text)
    except:
        return 0.0


# ==========================================================
# MEMBERSIHKAN DATA
# ==========================================================

def clean_dataframe(df):

    data = df.copy()

    # Bersihkan kolom waktu persiapan
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

    # Pastikan kolom numerik
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
# FITUR UNTUK K-MEANS
# ==========================================================

def get_feature_columns():
    """
    Fitur yang digunakan dalam proses clustering.
    """

    return [
        "Total_harga",
        "Jumlah_pesanan",
        "rata_rata_harga",
        "waktu_persiapan_yang_diberikan",
        "waktu_persiapan_digunakan"
    ]


# ==========================================================
# STANDARD SCALER
# ==========================================================

def preprocess_data(df):
    """
    Membersihkan data dan melakukan StandardScaler.
    """

    data = clean_dataframe(df)

    feature_columns = get_feature_columns()

    X = data[feature_columns].copy()

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    scaled_df = pd.DataFrame(
        X_scaled,
        columns=feature_columns
    )

    return scaled_df, scaler


# ==========================================================
# MENGEMBALIKAN DATA BERSIH TANPA SCALING
# ==========================================================

def get_clean_data(df):

    return clean_dataframe(df)


