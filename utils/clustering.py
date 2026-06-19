import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# ==========================================================
# ELBOW METHOD
# ==========================================================

def elbow_method(X_scaled, max_k=10):
    """
    Mengembalikan DataFrame berisi nilai WCSS
    untuk K = 2 sampai max_k.
    """

    if len(X_scaled) < 2:
        return pd.DataFrame(columns=["K", "WCSS"])

    max_cluster = min(max_k, len(X_scaled))

    hasil = []

    for k in range(2, max_cluster + 1):

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)

        hasil.append({
            "K": k,
            "WCSS": model.inertia_
        })

    return pd.DataFrame(hasil)


# ==========================================================
# MENJALANKAN K-MEANS
# ==========================================================

def run_kmeans(X_scaled):

    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    centroid = pd.DataFrame(
        model.cluster_centers_,
        columns=X_scaled.columns
    )

    return model, labels, centroid


# ==========================================================
# SILHOUETTE SCORE
# ==========================================================

def calculate_silhouette(X_scaled, labels):

    if len(set(labels)) < 2:
        return 0.0

    return float(
        silhouette_score(
            X_scaled,
            labels
        )
    )


# ==========================================================
# MENAMBAHKAN LABEL CLUSTER
# ==========================================================

def add_cluster_result(df, labels):

    hasil = df.copy()

    hasil["cluster"] = labels

    return hasil


# ==========================================================
# INTERPRETASI CLUSTER DINAMIS
# ==========================================================

def add_interpretation(df, centroid):

    urutan = (
        centroid["Total_harga"]
        .sort_values()
        .index
        .tolist()
    )

    mapping = {
        urutan[0]: "Pola Pemesanan Personal",
        urutan[1]: "Pola Pemesanan Reguler",
        urutan[2]: "Pola Pemesanan Kelompok"
    }

    hasil = df.copy()

    hasil["Interpretasi"] = (
        hasil["cluster"]
        .map(mapping)
    )

    return hasil


# ==========================================================
# RINGKASAN CLUSTER
# ==========================================================

def cluster_summary(df):

    summary = (
        df.groupby("Interpretasi")
        .size()
        .reset_index(name="Jumlah Data")
    )

    return summary


# ==========================================================
# RATA-RATA SETIAP CLUSTER
# ==========================================================

def cluster_statistics(df):

    hasil = (
        df.groupby("Interpretasi")[
            [
                "Total_harga",
                "Jumlah_pesanan",
                "rata_rata_harga",
                "waktu_persiapan_yang_diberikan",
                "waktu_persiapan_digunakan"
            ]
        ]
        .mean()
        .round(2)
        .reset_index()
    )

    return hasil

