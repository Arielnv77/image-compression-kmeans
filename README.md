# Image Compression Using K-Means Clustering

This project explores how unsupervised learning can be applied to compress images by reducing the number of unique colors they contain.
Using the K-Means clustering algorithm, the image is reconstructed with a simplified color palette while preserving its overall appearance.
The goal is to demonstrate how a classic ML technique can be used in a practical, visual way.

⸻

# Purpose of the Project

The idea behind this work is to show that machine learning is not limited to predictions — it can also help reduce data complexity.

By grouping similar colors together, K-Means learns the dominant tones in an image.
Once those clusters are formed, each pixel is replaced with the color of the cluster it belongs to.
The result is a compressed version of the image that uses fewer colors while maintaining most of the visual structure.

This technique is widely used in:
	•	Basic image compression
	•	Texture simplification
	•	Preprocessing for computer vision tasks
	•	Color quantization

⸻
# How It Works

The compression process follows these steps:

1. Load and preprocess the image

The original image is read, converted to RGB, and transformed into a NumPy array.
Each pixel becomes a vector of three values representing its color in RGB space.

2. Flatten the image data

The pixel matrix (height, width, 3) is reshaped into a list of points (num_pixels, 3).
This allows K-Means to treat each pixel as a sample in a 3-dimensional space.

3. Apply K-Means with different values of k

The model is trained using several cluster counts (2, 4, 8, 16, 32).
Each k value represents the number of colors allowed in the compressed image.

4. Reconstruct the compressed image

After clustering, every pixel is replaced by the centroid of its assigned cluster.
The final result is reshaped back to the original image size.

5. Measure compression

A simple compression ratio is computed using:
	•	original color space
	•	number of clusters
	•	bits needed to encode each pixel’s cluster index

6. Visualize the results

A comparison grid shows how the image looks for each value of k, making it easy to see the balance between quality and compression.


# Results

Running the notebook generates:
	•	The original image
	•	Five compressed versions using different values of k
	•	A table showing:
	•	compressed size estimate
	•	compression ratio for each version
	•	A combined comparison figure displaying all images side by side

The results clearly show how lowering the number of colors increases the compression factor, while higher values of k retain more detail and smoother gradients.
