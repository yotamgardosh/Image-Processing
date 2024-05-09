import cv2
import numpy as np


def load_images(low_res_path, high_res_path):
    low_res_image = cv2.imread(low_res_path)
    high_res_part = cv2.imread(high_res_path)
    return low_res_image, high_res_part


def detect_and_compute_features(image):
    detector = cv2.SIFT_create()
    keypoints, descriptors = detector.detectAndCompute(image, None)
    return keypoints, descriptors


def match_features(des1, des2, threshold=0.6):
    matcher = cv2.BFMatcher()
    matches = matcher.knnMatch(des1, des2, k=2)
    # fnn and snn = first and second nearest neighbor
    good_matches = [fnn for fnn, snn in matches if fnn.distance < threshold * snn.distance]
    return good_matches


def find_homography(kp1, kp2, matches):
    src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    homography, _ = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC)
    return homography


def create_mask(image, threshold=10):
    """Assuming image is grayscale, create a binary mask where pixels > threshold are True."""
    if len(image.shape) == 3 and image.shape[2] == 4:  # Has alpha channel
        alpha_channel = image[:, :, 3]
        mask = alpha_channel > threshold
    else:  # Convert to grayscale and apply threshold
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)
        mask = mask > threshold
    return mask.astype(np.uint8)


def mask_blend_images(low_res_image, warped_high_res, mask):
    """Blend images based on a binary mask."""
    blended_image = np.where(mask[:, :, None] == 1, warped_high_res, low_res_image)
    return blended_image


def warp_and_blend_images(low_res_image, high_res_image, H):
    height, width = high_res_image.shape[:2]
    warped_high_res = cv2.warpPerspective(high_res_image, H, (width, height))
    # Assuming you want to create a mask from the high_res_part or its warped version
    mask = create_mask(warped_high_res, threshold=9)  # 9 is best after testing

    blended_image = mask_blend_images(low_res_image, warped_high_res, mask)
    return blended_image


def draw_matches(img1, kp1, img2, kp2, matches):
    return cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


def main(low_res_path, high_res_path, file_name, nearest_neighbor=0.6):
    low_res_image, high_res_image = load_images(low_res_path, high_res_path)

    kp_low, des_low = detect_and_compute_features(low_res_image)
    kp_high, des_high = detect_and_compute_features(high_res_image)

    good_matches = match_features(des_low, des_high, nearest_neighbor)
    matched_vis = draw_matches(low_res_image, kp_low, high_res_image, kp_high, good_matches)
    # Resize for display if needed
    display_size = (800, 600)  # Set this to your desired window size
    matched_vis_resized = cv2.resize(matched_vis, display_size, interpolation=cv2.INTER_AREA)

    cv2.imshow('Matched Features', matched_vis_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.imwrite('matches_vis_{name}.jpg'.format(name=file_name), matched_vis_resized)

    # Estimate homography and blend images
    H = find_homography(kp_low, kp_high, good_matches)
    if H is None:
        print("Could not find a valid homography.")
    else:
        blended_image = warp_and_blend_images(low_res_image, high_res_image, H)
        blended_image_resized = cv2.resize(blended_image, display_size, interpolation=cv2.INTER_AREA)
        cv2.imshow('Blended Image', blended_image_resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # cv2.imwrite('blended_result_{name}.jpg'.format(name=file_name), blended_image)


if __name__ == '__main__':
    main('inputs/lake_low_res.jpg', 'inputs/lake_high_res.png', 'desert', 0.75)
