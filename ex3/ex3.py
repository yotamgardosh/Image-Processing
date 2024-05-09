import cv2
import numpy as np

def construct_gaussian_pyramid(image, levels=5):
    pyramid = [image.astype(float)]
    for _ in range(levels):
        image = cv2.pyrDown(image)
        # cv2.imwrite('results/gaussian_pyramid_{i}.jpg'.format(i=_), image)
        pyramid.append(image.astype(float))
    return pyramid

def construct_laplacian_pyramid(gaussian_pyramid):
    laplacian_pyramid = []
    for i in range(len(gaussian_pyramid) - 1):
        expanded = cv2.pyrUp(gaussian_pyramid[i + 1])
        laplacian = gaussian_pyramid[i] - expanded
        cv2.imwrite('results/laplacian_pyramid_{i}.jpg'.format(i=i), laplacian)
        laplacian_pyramid.append(laplacian)
    laplacian_pyramid.append(gaussian_pyramid[-1])  # Append the last level of Gaussian pyramid
    return laplacian_pyramid

def blend_pyramids(laplacian_pyramid1, laplacian_pyramid2, mask):
    blended_pyramid = []
    for l1, l2, m in zip(laplacian_pyramid1, laplacian_pyramid2, mask):
        blended = l1 * m + l2 * (1 - m)
        blended_pyramid.insert(0, blended)
    return blended_pyramid

def reconstruct_image_from_pyramid(blended_pyramid):
    blended_image = blended_pyramid[0]
    for i in range(1, len(blended_pyramid)):
        blended_image = cv2.pyrUp(blended_image)
        blended_image += blended_pyramid[i]
    return np.clip(blended_image, 0, 255).astype('uint8')

def reformat_mask(mask):
    color_mask = np.zeros((mask.shape[0], mask.shape[1], 3), dtype=np.uint8)
    color_mask[mask == 0] = (0, 0, 0)
    color_mask[mask == 255] = (1, 1, 1)
    return color_mask

def create_blended_image(image1, image2, mask, image_dim=(512,512), levels=5):
    #resize images and mask
    image1 = cv2.resize(image1, image_dim)
    image2 = cv2.resize(image2, image_dim)
    mask = cv2.resize(mask, image_dim)

    #transform mask to 3 dim image to match images
    color_mask = reformat_mask(mask)

    # Construct Gaussian pyramids
    gaussian_pyramid1 = construct_gaussian_pyramid(image1, levels)
    gaussian_pyramid2 = construct_gaussian_pyramid(image2, levels)
    gaussian_mask = construct_gaussian_pyramid(color_mask, levels)

    # Construct Laplacian pyramids
    laplacian_pyramid1 = construct_laplacian_pyramid(gaussian_pyramid1)
    laplacian_pyramid2 = construct_laplacian_pyramid(gaussian_pyramid2)

    # Blend pyramids
    blended_pyramid = blend_pyramids(laplacian_pyramid1, laplacian_pyramid2, gaussian_mask)

    # Reconstruct blended image
    result = reconstruct_image_from_pyramid(blended_pyramid)
    return result

def create_hybrid_image(image1, image2, target_size=(1024, 1024)):
    # resize images
    image1 = cv2.resize(image1, target_size)
    image2 = cv2.resize(image2, target_size)

    # Build Gaussian pyramids
    gaussian_pyramid1 = construct_gaussian_pyramid(image1,5)
    gaussian_pyramid2 = construct_gaussian_pyramid(image2,5)

    # Build Laplacian pyramids
    laplacian_pyramid1 = construct_laplacian_pyramid(gaussian_pyramid1)
    laplacian_pyramid2 = construct_laplacian_pyramid(gaussian_pyramid2)

    # Construct hybrid pyramid
    hybrid_pyramid = construct_hybrid_pyramid(laplacian_pyramid1, laplacian_pyramid2)
    hybrid_image = reconstruct_image_from_pyramid(hybrid_pyramid)

    return hybrid_image

def construct_hybrid_pyramid(laplacian_pyramid1, laplacian_pyramid2, cutoff=4):
    # Construct hybrid pyramid
    hybrid_pyramid = []
    num_of_levels = len(laplacian_pyramid1)
    for i in range(num_of_levels):
        insert_val = laplacian_pyramid1[i] if i < cutoff else laplacian_pyramid2[i]
        hybrid_pyramid.insert(0, insert_val)
    return hybrid_pyramid

def q1():
    # Load images and mask
    image1 = cv2.imread('images/spiderman.png')
    image2 = cv2.imread('images/spiderman.png')
    mask = cv2.imread('images/zebra_mask.jpg', cv2.IMREAD_GRAYSCALE)

    # Perform blending
    result = create_blended_image(image1, image2, mask)

    # save result
    cv2.imwrite('results/blended_img_bad.jpg', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def q2():

    image1 = cv2.imread('images/arch_stars.jpg')
    image2 = cv2.imread('images/arch_stars.jpg')

    # Perform hybrid blending
    result = create_hybrid_image(image1, image2)

    # save result
    cv2.imwrite('results/hybrid_img_good.jpg', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # q1()
    q2()
