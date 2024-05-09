# Image Blending and Hybrid Image Creation

Repository for Exercise 3 of the Image Processing course, which involves the creation of blended and hybrid images using the techniques of image pyramids and frequency domain manipulation.


# Exercise Objectives

The main objectives of this exercise are:

* To seamlessly blend two images using a given mask.
* To create a hybrid image where one image is visible at close range, and another is visible from a distance.
These objectives are achieved by manipulating image frequencies through Gaussian and Laplacian pyramids for image blending and by employing high-pass and low-pass filtering in the frequency domain for hybrid images.

# Methodology
The exercise is based on the principle that images can be represented and manipulated at different frequency levels to achieve various effects:

Image Blending
1. Load two images and a binary mask.
2. Create Gaussian pyramids for each image.
3. Construct Laplacian pyramids for blending.
4. Reconstruct the blended image from the blended pyramid.

Hybrid Images
1. Load two images to be combined.
2. Transform each image into the frequency domain.
3. Apply a high-pass filter to the first image and a low-pass filter to the second image.
4. Combine the images in the frequency domain.
5. Transform the combined image back into the spatial domain.

# Conclusion
This exercise explores the power and limitations of image processing using simple algorithms. The resulting images underscore the impact of choosing appropriate blending masks, image pairs, and parameter settings.
