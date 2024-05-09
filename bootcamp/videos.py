import mediapy as media
import numpy as np
import matplotlib.pyplot as plt

def video():
    url = "C:/University/CS/Image_Processing/bootcamp/video1_category1.mp4"
    vid = media.read_video(url)
    print("shape:",vid.shape,"data type:", vid.dtype)
    print(vid.metadata)
    # print(vid)
    media.show_video()
    # media.show_video(vid)
    # print("123")



def main():
    video()

if __name__ == "__main__":
    main()