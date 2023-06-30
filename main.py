import sys

# import screen size utility module that helps us scale the "forest" based on device screen size
import pyautogui

import cv2 as cv
import numpy as np

from forest import Forest

# colours
green, light_green, brown = (40, 185, 40), (25, 220, 0), (30, 65, 155)


@staticmethod
def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


@staticmethod
def scaleBackground(screenPct: float) -> tuple[int, int]:
    # find out the width and height of the device we are running on
    device_width, device_height = pyautogui.size()

    # scale width and height based on what percentage of device size user wants to use, rounded to
    # the nearest multiple of 100
    scaledWidth: int = int((device_width * screenPct // 100) * 100)
    scaledHeight: int = int((device_height * screenPct // 100) * 100)

    return scaledWidth, scaledHeight


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')

    # general parameters
    n_trees = 30

    # scale the size of the background based on device size
    width, height = scaleBackground(0.75)
    print(f'scaled: width={width}, height={height}')

    # blank, scaled image
    bg = np.zeros((height, width, 3), dtype=np.uint8)

    # create a forest by passing the scaled, empty image to the constructor
    forest = Forest(bg)

    # sky
    forest.draw_sky()

    # ground
    forest.draw_ground()

    # display image
    cv.imshow('forest of objects', bg)

    cv.waitKey(0)
    cv.destroyAllWindows()
