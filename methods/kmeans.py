import numpy as np


class CosineKMeans:
    """
    A K-means clustering algorithm variant using cosine similarity.

    Attributes:
        n_clusters (int): Number of clusters.
        max_iter (int): Maximum number of iterations for the algorithm.
        centroids (np.array): Array of centroids for the clusters.
        labels (np.array): Array of cluster labels for each data point.
    """
    def __init__(self, n_clusters=7, max_iter=300, random_seed = None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_seed = random_seed
        self.__centroids = None  
        self.__labels = None    
        
    def normalize(self, X):
        norm = np.linalg.norm(X, axis=1, keepdims=True)
        return X / norm

    def closest_centroid(self, X):
        similarity = np.dot(X, self.__centroids.T)  # Cosine similarity
        return np.argmax(similarity, axis=1)

    def compute_centroids(self, X, labels):
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            centroids[k, :] = np.mean(X[labels == k, :], axis=0)
        return self.normalize(centroids)

    def fit(self, X):
        np.random.seed(self.random_seed)
        
        # Normalize the data
        X = self.normalize(X)

        # Initialize centroids
        random_idx = np.random.permutation(X.shape[0])
        self.__centroids = X[random_idx[:self.n_clusters], :]

        # Iterate to update centroids and labels
        for _ in range(self.max_iter):
            labels = self.closest_centroid(X)
            new_centroids = self.compute_centroids(X, labels)

            # Check for convergence (if centroids do not change)
            if np.all(new_centroids == self.__centroids):
                break
            self.__centroids = new_centroids

        self.__labels = labels

    def get_centroids(self):
        if self.__centroids is None:
            raise RuntimeError("Fit method has not been called yet.")
        return self.__centroids

    def get_labels(self):
        if self.__labels is None:
            raise RuntimeError("Fit method has not been called yet.")
        return self.__labels