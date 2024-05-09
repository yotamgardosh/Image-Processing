# High-Resolution Image Blending
Repository of Exercise 4 of the Image Processing course, where we focus on blending high-resolution segments seamlessly into low-resolution images using various image processing techniques.

# Exercise Overview
This exercise challenges us to integrate high-resolution parts of an image into their corresponding low-resolution counterparts. The task involves using feature extraction, feature matching, RANSAC for homography estimation, and image warping to achieve a seamless blend.

# Methodology
The approach involves several steps:

1. Feature Extraction and Matching: Identifies key points and matches them between the high and low-resolution images.
2. RANSAC Homography Estimation: Robustly estimates a transformation matrix to align the images.
3. Image Warping: Aligns the high-resolution segment with the low-resolution image.
4. Blending: Smoothly integrates the aligned high-resolution details into the low-resolution base.

## Detailed Algorithm Steps:
1. Load the images and identify keypoints using SIFT.
2. Match features between images, filtering by distance ratio.
3. Estimate a homography matrix with RANSAC to align images accurately.
4. Apply backward warping to align the high-resolution image with the low-resolution image's perspective.
5. Create a binary mask for blending from the warped image.
6. Perform pyramid blending to merge images seamlessly.

# Conclusion
This exercise illustrates the practical application of complex image processing techniques to combine images of different resolutions. It demonstrates the effectiveness of feature-based image registration and the challenges posed by blending disparate resolution images.
