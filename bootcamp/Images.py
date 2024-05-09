from PIL import Image
import numpy as np
from skimage import io, color
import matplotlib.pyplot as plt

def with_PIL():
    #Q1
    cool_cat = Image.open("cool_cat_image.jpg")
    np_cool_cat = np.array(cool_cat)

    #Q2
    print(np_cool_cat.shape)
    print(np_cool_cat.dtype)

    #Q3
    plt.imshow(cool_cat)
    plt.show()

    #Q4
    gray_cat = cool_cat.convert("L")

    #Q5
    np_gray_cat = np.array(gray_cat)
    print(np_gray_cat.shape)

    #Q6
    plt.imshow(gray_cat, cmap='gray')
    plt.show()

    #Q7
    gray_cat.save("./gray_cat.jpg")

    #Q8
    np_cool_cat_float32 = np_cool_cat / 255.0

    #Q9
    mean = np_cool_cat_float32.mean()
    np_cool_cat_float32_normalized = np_cool_cat_float32 - mean

    #Q10
    np_cool_cat_float32_normalized_0to1 =(np_cool_cat_float32_normalized - np.min(np_cool_cat_float32_normalized)) / np.max(np_cool_cat_float32_normalized) - np.min(np_cool_cat_float32_normalized)

    #Q11
    back_to_cool_cat = (np_cool_cat_float32_normalized_0to1 * 255).astype(np.uint8)
    back_to_cool_cat = Image.fromarray(back_to_cool_cat)

    #Q12
    fig, axes = plt.subplots(1,3, figsize=(12,4))

    axes[0].imshow(cool_cat)
    axes[0].set_title('Original RGB Image')

    axes[1].imshow(gray_cat,cmap='gray')
    axes[1].set_title('Grayscale Image')

    axes[2].imshow(back_to_cool_cat)
    axes[2].set_title('Manipulated RGB Image')

    plt.show()

def with_skimage():
    #Q1
    rgb_cat = io.imread("cool_cat_image.jpg")

    #Q2
    print(rgb_cat.shape)
    print(rgb_cat.mean())

    #Q3
    plt.imshow(rgb_cat)
    # plt.show()

    #Q4
    gray_cat = color.rgb2gray(rgb_cat)

    #Q5
    print(gray_cat.shape)
    print(gray_cat.dtype)

    #Q6
    plt.imshow(gray_cat,cmap='gray')
    # plt.show()

    #Q7
    back_to_correct_range_and_type = (gray_cat * 255).astype(np.uint8)
    io.imsave("graycat.jpg", back_to_correct_range_and_type)

    #Q8
    sig_rgb_cat = (rgb_cat / 255.0)

    #Q9
    mean = np.mean(sig_rgb_cat)
    print("Mean before subtraction:", mean)
    sub_mean = sig_rgb_cat - mean
    print("Mean after subtraction:", np.mean(sub_mean))

    #Q10
    back_to_0_1 = (sub_mean - np.min(sub_mean)) / (np.max(sub_mean) - np.min(sub_mean))

    #Q11
    back_to_255 = (back_to_0_1 * 255.0).astype(np.uint8)
    # Print some statistics
    print("Statistics of back_to_255:")
    print("Min:", np.min(back_to_255))
    print("Max:", np.max(back_to_255))
    print("Mean:", np.mean(back_to_255))

    # Visualize the manipulated image
    plt.imshow(back_to_255)
    plt.title("Manipulated Image")
    plt.show()
    #Q12
    fig, axes = plt.subplots(1,3,figsize=(12,4))

    axes[0].imshow(rgb_cat)
    axes[0].set_title("original")

    axes[1].imshow(gray_cat,cmap='gray')
    axes[1].set_title("gray")

    axes[2].imshow(back_to_255)
    axes[2].set_title("manipulated")

    plt.show()







def main():
    with_PIL()
    # with_skimage()

if __name__ == "__main__":
    main()