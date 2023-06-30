import cv2 as cv
import numpy as np

class Forest:
    def __init__(self, image, width, height):
        self.bg = image
        self.width = width
        self.height = height
        # ground
        self.ground_level = int(height * 0.15 * 10 / 10)
        self.groundColor = (75, 180, 70)
        self.groundThickness = -1
        # sky
        self.skyColor = (255, 255, 85)  # BGR, not RGB
        self.skyLineThickness = -1

    def draw_sky(self):
        x1, y1 = 0, 0
        x2, y2 = self.width, self.height - self.ground_level
        print(f'ground level={self.ground_level}, y2={y2}')
        cv.rectangle(self.bg, (x1, y1), (x2, y2), self.skyColor, self.skyLineThickness)

    def draw_ground(self):
        x1, y1 = 0, self.height - self.ground_level
        x2, y2 = self.width, self.height
        cv.rectangle(self.bg, (x1, y1), (x2, y2), self.groundColor, self.groundThickness)