# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 16:29:25 2023

@author: imvia
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a 1D signal (example: a sinusoidal signal)
t = np.linspace(0, 1, 1000)  # Time vector from 0 to 1 with 1000 samples
frequency = 5  # Frequency of the sinusoidal signal
signal = np.sin(2 * np.pi * frequency * t)

# Compute the Fourier Transform
fourier_transform = np.fft.fft(signal)
frequency_values = np.fft.fftfreq(len(t))

# Shift the zero frequency component to the center
fourier_transform = np.fft.fftshift(fourier_transform)
frequency_values = np.fft.fftshift(frequency_values)

# Plot the original signal and its Fourier Transform
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(122)
plt.plot(frequency_values, np.abs(fourier_transform))
plt.title('Fourier Transform')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
