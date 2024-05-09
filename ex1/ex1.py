import numpy as np
import mediapy as media
import matplotlib.pyplot as plt

GREYSCALE_TRANSFORMER = [0.299, 0.587, 0.114]



def transform_to_greyscale(rgb_video):
    gray_video = []
    number_of_frames = rgb_video.shape[0]
    for i in range(number_of_frames):
        gray_video.append(rgb_video[i] @ GREYSCALE_TRANSFORMER)
    return np.array(gray_video)


def integrate_hist(hist):
    # Calculate the cumulative sum of the histogram
    cumulative_sum = np.cumsum(hist)

    # Sum up the cumulative sum to get the total integrated value
    total_integrated_value = np.sum(cumulative_sum)

    return total_integrated_value


def analyze_dist_data(arr, video_path):
    """
    Analyze the given array of distances.

    Parameters:
    - arr (numpy.ndarray): Array of distances.

    Returns:
    - dict: Dictionary containing statistical information.
    """

    # Calculate statistics
    min_dist = np.min(arr)
    mean_dist = np.mean(arr)
    max_dist = np.max(arr)

    # Find the index of the maximum distance
    max_dist_index = np.argmax(arr)

    # Create a scatter plot
    plt.scatter(range(len(arr)), arr, label='Distances')

    # Highlight the point with the maximum distance
    plt.scatter(max_dist_index, max_dist, color='red', label='Max Distance')

    # Draw a vertical line to highlight the maximum distance index on the x-axis
    plt.axvline(x=max_dist_index, color='red', linestyle='--', label='Max Distance Index')

    # Set labels and legend
    plt.xlabel('Index')
    plt.ylabel('Distance')
    plt.legend()
    plt.title(f'Scatter Plot of Distances {video_path}')

    # Show the plot
    plt.show()

    print("Statistical Information:")
    print(f"Min Distance: {min_dist:.2f}")
    print(f"Mean Distance: {mean_dist:.2f}")
    print(f"Max Distance: {max_dist:.2f} (Index: {max_dist_index})")

def show_results(video_path,scene_one, scene_two):
    print(str(scene_one) + " , " + str(scene_two))
    video = media.read_video(video_path)
    frame_one = video[scene_one]
    frame_two = video[scene_two]
    plt.imshow(frame_one)
    plt.show()
    plt.imshow(frame_two)
    plt.show()



def main(video_path, video_type):
    """
    Main entry point for ex1
    :param video_path: path to video file
    :param video_type: category of the video (either 1 or 2)
    :return: a tuple of integers representing the frame number for which the scene cut was detected (i.e. the last frame index of the first scene and the first frame index of the second scene)
    """

    rgb_video = media.read_video(video_path)
    ans = [0,1]
    max_dist = float('-inf')
    dist_arr = []

    gray_scale_video = transform_to_greyscale(rgb_video)

    number_of_frames = gray_scale_video.shape[0]
    for i in range(number_of_frames-1):
        cur_frame_hist, _ = np.histogram(gray_scale_video[i], bins=255)
        next_frame_hist, _ = np.histogram(gray_scale_video[i+1], bins=255)

        integrated_cur_frame_hist = integrate_hist(cur_frame_hist)
        integrated_next_frame_hist = integrate_hist(next_frame_hist)
        dist = np.abs(integrated_cur_frame_hist - integrated_next_frame_hist)
        dist_arr.append(dist)
        if dist > max_dist:
            max_dist = dist
            ans[0], ans[1] = i, i+1

    analyze_dist_data(dist_arr, video_path)
    return tuple(ans)


if __name__ == "__main__":

    path_arr = ['video1_category1.mp4',
                'video2_category1.mp4',
                'video3_category2.mp4',
                'video4_category2.mp4']
    frame_arr = []

    for path in path_arr:
        frame_arr.append(main(path,1))

    for i in range(len(frame_arr)):
        show_results(path_arr[i], frame_arr[i][0],frame_arr[i][1])


