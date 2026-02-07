
Project Overview: BioVector is a comprehensive pipeline for fingerprint analysis and recognition. It transforms raw biometric images into quantized feature vectors, enabling efficient matching and identification within a database.

Technical Workflow & Implementation:

Image Enhancement: Implements Adaptive Thresholding (Gaussian) and Histogram Equalization to improve the clarity of ridge patterns and remove noise.

Feature Extraction: Uses the Harris Corner Detection algorithm to identify key minutiae points on the fingerprint, converting visual data into numerical feature vectors.

Noise Reduction: Employs Median Blur filters to ensure the accuracy of corner detection by eliminating salt-and-pepper noise.

Vector Quantization: Utilizes K-Means Clustering from the scipy library to create "codebooks," allowing for the quantization of complex feature vectors into manageable codes.

Recognition Logic: Features a verification module that compares new fingerprint codes against a pre-existing database to determine identity with statistical confidence.

Technical Stack:

Language: Python.

Computer Vision: OpenCV (cv2), Scikit-image.

Data Science: NumPy, SciPy (Cluster/VQ).

