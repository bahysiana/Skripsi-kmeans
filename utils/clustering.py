import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ==========================================================
# ELBOW METHOD
# ==========================================================

def elbow_method(X_scaled, max_k=10):

    wcss = []

    max_cluster = min(max_k, len(X_scaled))

    for k in range(2, max_cluster + 1):

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)

        wcss.append(model.inertia_)

    return pd.DataFrame({
        "K": list(range(2, max_cluster + 1)),
        "WCSS": wcss
    })


# ==========================================================
# K-MEANS (K = 3)
# ==========================================================

def run_kmeans(X_scaled):

    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    centroids = pd.DataFrame(
        model.cluster_centers_,
        columns=X_scaled.columns
    )

    return model, labels, centroids


# ==========================================================
# SILHOUETTE SCORE
# ==========================================================

def calculate_silhouette(X_scaled, labels):

    if len(set(labels)) <= 1:
        return 0.0

    return float(
        silhouette_score(
            X_scaled,
            labels
        )
    )


# ==========================================================
# MENAMBAHKAN CLUSTER KE DATA
# ==========================================================

def add_cluster_result(df, labels):

    hasil = df.copy()

    hasil["cluster"] = labels

    return hasil


# ==========================================================
# RINGKASAN CLUSTER
# ==========================================================

def cluster_summary(df):

    return (
        df.groupby("cluster")
        .size()
        .reset_index(name="Jumlah Data")
        .sort_values("cluster")
    )


# ==========================================================
# STATISTIK CLUSTER
# ==========================================================

def cluster_statistics(df):

    return (
        df.groupby("cluster")[
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


# ==========================================================
# LABEL CLUSTER
# ==========================================================

def add_cluster_label(df):

    mapping = {
        0: "Cluster 1",
        1: "Cluster 2",
        2: "Cluster 3"
    }

    hasil = df.copy()

    hasil["Label"] = hasil["cluster"].map(mapping)

    return hasil

