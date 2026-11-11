# Lab 7 – Explainable AI, Adversarial AI, PCA and SVD

## Aim
To understand Explainable AI, Adversarial AI, dimensionality reduction, and matrix decomposition using Python.

## Problem Statement
To implement a CNN-based image classification project and demonstrate Grad-CAM, FGSM, PCA, and SVD techniques.

## Tools and Libraries
- Python
- PyTorch
- NumPy
- Matplotlib
- Pillow

## Experiments Performed

### 1. CNN Image Classification
Created a dataset containing images of circles and squares and trained a Convolutional Neural Network (CNN) to classify the shapes.

### 2. Grad-CAM
Generated a heatmap to identify the important image regions that influence the CNN's classification decision.

### 3. FGSM
Applied the Fast Gradient Sign Method (FGSM) to generate an adversarial image by slightly modifying the input pixels using gradients.

### 4. PCA
Used Principal Component Analysis (PCA) to reduce image features from 1024 dimensions to 2 principal components for visualization.

### 5. SVD
Applied Singular Value Decomposition (SVD) to decompose an image matrix and reconstruct the image using the first five singular values.

## Results
- Successfully trained a CNN for shape classification.
- Generated Grad-CAM heatmaps to visualize important image regions.
- Applied FGSM to create an adversarial image.
- Reduced image dimensions using PCA.
- Reconstructed an image using SVD.

## Output Files
- `training_loss.png`
- `gradcam_visualization.png`
- `fgsm_attack.png`
- `pca_visualization.png`
- `svd_visualization.png`
- `training_output.png`

## Learning Outcomes
- Understood CNN-based image classification.
- Learned the importance of Explainable AI.
- Understood Grad-CAM visualization.
- Learned how adversarial attacks work using FGSM.
- Understood dimensionality reduction using PCA.
- Learned matrix decomposition and image reconstruction using SVD.

## Conclusion
This experiment demonstrated image classification using Convolutional Neural Networks and explored model explainability, adversarial attacks, dimensionality reduction, and image reconstruction techniques.