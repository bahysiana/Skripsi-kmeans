import pandas as pd

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# =====================================================
# MENJALANKAN K-MEANS
# =====================================================

def run_kmeans(data_scaled, n_clusters=3):
    """
    Menjalankan algoritma K-Means.
    """

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(data_scaled)

    centroids = pd.DataFrame(
        model.cluster_centers_,
        columns=data_scaled.columns
    )

    return model, labels, centroids


# =====================================================
# MENGHITUNG SILHOUETTE SCORE
# =====================================================

def calculate_silhouette(data_scaled, labels):
    """
    Menghitung Silhouette Score.
    """

    if len(set(labels)) < 2:
        return 0

    return silhouette_score(
        data_scaled,
        labels
    )


# =====================================================
# MENAMBAHKAN LABEL CLUSTER
# =====================================================

def add_cluster_to_dataframe(df, labels):
    """
    Menambahkan kolom cluster ke DataFrame.
    """

    hasil = df.copy()

    hasil["Cluster"] = labels

    return hasil


# =====================================================
# RINGKASAN CLUSTER
# =====================================================

def cluster_summary(df_cluster):
    """
    Membuat ringkasan jumlah data tiap cluster.
    """

    summary = (
        df_cluster["Cluster"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    summary.columns = [
        "Cluster",
        "Jumlah Data"
    ]

    mapping = {
        0: "Pola Pemesanan Personal",
        1: "Pola Pemesanan Reguler",
        2: "Pola Pemesanan Kelompok"
    }

    summary["Interpretasi"] = (
        summary["Cluster"]
        .map(mapping)
    )

    return summary
