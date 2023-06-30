import cv2 as cv
import numpy as np

class Forest:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # ground
        self.ground_level = int(height * 0.15 * 10 / 10)
        self.groundColor = (75, 180, 70)
        self.groundThickness = -1
        # sky
        self.skyColor = (255, 255, 85)  # BGR, not RGB
        self.skyLineThickness = -1

