# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:48:41 2023

@author: imvia
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'coin.png'  # Replace with the path to your image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform the 2D Fourier Transform
fourier_transform = np.fft.fft2(image)
fourier_transform_shifted = np.fft.fftshift(fourier_transform)
magnitude_spectrum = np.log(np.abs(fourier_transform_shifted) + 1)

# Display the original and Fourier transformed images
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.axis('off')
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Fourier Transform Magnitude'), plt.axis('off')
plt.show()
