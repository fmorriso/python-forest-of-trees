import sys

# import screen size utility module that helps us scale the "forest" based on device screen size
import pyautogui

import cv2 as cv
import numpy as np
from numpy import ndarray

from forest import Forest
from tree import Tree

# colours
green, light_green, brown = (40, 185, 40), (25, 220, 0), (30, 65, 155)


@staticmethod
def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

#
@staticmethod
def scaleBackground(screenPct: float) -> tuple[int, int]:
    # find out the width and height of the device we are running on
    device_width, device_height = pyautogui.size()

    # scale width and height based on what percentage of device size user wants to use, rounded to
    # the nearest multiple of 100
    scaled_width: int = int((device_width * screenPct // 100) * 100)
    scaled_height: int = int((device_height * screenPct // 100) * 100)

    return scaled_width, scaled_height


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')

    # general parameters
    n_trees: int = 30

    # scale the size of the background to a percentage of the device size
    width, height = scaleBackground(0.75)
    print(f'scaled: width={width}, height={height}')

    # blank, scaled image
    bg: ndarray = np.zeros((height, width, 3), dtype=np.uint8)

    # create a forest by passing the scaled, empty image to the constructor
    forest = Forest(bg)

    # background
    forest.draw_background()

    # trees
    #forest.bg = Tree(forest, bg, 0.50).draw()
    forest.draw_tree( Tree(bg, 0.50) )

    # display image
    cv.imshow('forest of objects', bg)

    cv.waitKey(0)
    cv.destroyAllWindows()
