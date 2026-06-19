```python
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# ==========================================================
# ELBOW METHOD
# ==========================================================

def elbow_method(data_scaled, max_k=10):

    wcss = []

    for k in range(2, max_k + 1):

        model = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        model.fit(data_scaled)

        wcss.append(model.inertia_)

    hasil = pd.DataFrame({
        "K": list(range(2, max_k + 1)),
        "WCSS": wcss
    })

    return hasil


# ==========================================================
# MENJALANKAN K-MEANS
# ==========================================================

def run_kmeans(data_scaled):

    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(data_scaled)

    centroid = pd.DataFrame(
        model.cluster_centers_,
        columns=data_scaled.columns
    )

    return model, labels, centroid


# ==========================================================
# SILHOUETTE SCORE
# ==========================================================

def calculate_silhouette(data_scaled, labels):

    if len(set(labels)) < 2:
        return 0.0

    return silhouette_score(
        data_scaled,
        labels
    )


# ==========================================================
# MENAMBAHKAN LABEL CLUSTER
# ==========================================================

def add_cluster_result(df, labels):

    hasil = df.copy()

    hasil["cluster"] = labels

    return hasil


# ==========================================================
# INTERPRETASI CLUSTER
# ==========================================================

def add_interpretation(df):

    mapping = {
        0: "Pola Pemesanan Personal",
        1: "Pola Pemesanan Reguler",
        2: "Pola Pemesanan Kelompok"
    }

    hasil = df.copy()

    hasil["Interpretasi"] = hasil["cluster"].map(mapping)

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
```
