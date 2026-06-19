import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# =====================================================
# MENJALANKAN K-MEANS
# =====================================================

def run_kmeans(scaled_df, n_clusters=3):
    """
    Menjalankan K-Means Clustering.
    """

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(scaled_df)

    centroids = pd.DataFrame(
        model.cluster_centers_,
        columns=scaled_df.columns
    )

    return model, labels, centroids


# =====================================================
# SILHOUETTE SCORE
# =====================================================

def get_silhouette_score(scaled_df, labels):
    """
    Menghitung Silhouette Score.
    """

    if len(set(labels)) <= 1:
        return 0

    return silhouette_score(
        scaled_df,
        labels
    )


# =====================================================
# MENAMBAHKAN LABEL CLUSTER
# =====================================================

def add_cluster(df_original, labels):
    """
    Menambahkan hasil cluster ke DataFrame asli.
    """

    hasil = df_original.copy()

    hasil["cluster"] = labels

    return hasil


# =====================================================
# INTERPRETASI CLUSTER
# =====================================================

def add_cluster_interpretation(df):

    mapping = {
        0: "Pola Pemesanan Personal",
        1: "Pola Pemesanan Reguler",
        2: "Pola Pemesanan Kelompok"
    }

    hasil = df.copy()

    hasil["interpretasi_cluster"] = (
        hasil["cluster"].map(mapping)
    )

    return hasil


# =====================================================
# RINGKASAN CLUSTER
# =====================================================

def cluster_summary(df):

    summary = (
        df.groupby("interpretasi_cluster")
        .size()
        .reset_index(name="Jumlah Data")
    )

    return summary
