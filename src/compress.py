import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

def load_image(path):
    """Loads an image and returns it as a NumPy array (RGB)."""
    img = Image.open(path).convert("RGB")
    return np.array(img)


def apply_kmeans(img_array, k):
    """Applies K-Means to an image array and returns the compressed image."""
    h, w, _ = img_array.shape
    pixels = img_array.reshape(-1, 3)

    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(pixels)

    new_colors = kmeans.cluster_centers_[kmeans.labels_]
    compressed = new_colors.reshape(h, w, 3).astype(np.uint8)

    return compressed


def save_image(img_array, path):
    """Saves a NumPy image array to a given path."""
    Image.fromarray(img_array).save(path)


def compress_image(path_in, path_out, k):
    """
    Loads an image, applies K-Means compression with k colors,
    and saves the result.
    """
    img = load_image(path_in)
    compressed = apply_kmeans(img, k)
    save_image(compressed, path_out)

    return compressed