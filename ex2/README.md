# Audio Denoising
Repository for the Audio Denoising exercise, part of the Image Processing course. This project focuses on the application of Fast Fourier Transform (FFT) and Short-Time Fourier Transform (STFT) methods to remove noise from audio signals.

# Exercise Overview

The objective of this exercise is to enhance audio quality by reducing noise using frequency domain analysis. Two noisy audio samples, each with distinct noise characteristics, are provided. The task involves applying tailored denoising techniques to these samples to mitigate the disruptive noise without access to the clean audio.

# Methodology

The denoising process involves transforming the audio signal into the frequency domain using FFT and STFT. By analyzing the spectral data, the algorithms developed for this exercise effectively identify and suppress the noise components in the audio.

Key Steps for Each Algorithm:
For the First Audio (Q1):

1. Load the audio and apply FFT.
2. Identify and nullify the frequency with the highest magnitude.
3. Apply inverse FFT to reconstruct the denoised audio.

For the Second Audio (Q2):

1. Load the audio and apply STFT.
2. Isolate the noise in the specified time-frequency region.
3. Apply inverse STFT to reconstruct the denoised audio.

# Conclusion
This exercise demonstrated the power of spectral analysis for audio signal processing. The findings emphasized the need for different denoising strategies depending on the noise characteristics and the audio signal's context.
