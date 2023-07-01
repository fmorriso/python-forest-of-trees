import cv2 as cv
import numpy as np


class Forest:
    green, light_green, brown = (40, 185, 40), (25, 220, 0), (30, 65, 155)

    def __init__(self, image):
        self.bg = image
        print(f'shape={self.bg.shape}')  # rows/height, columns/width, dimensions
        print(f'rows/height={self.bg.shape[0]}')
        print(f'columns/width={self.bg.shape[1]}')
        self.width = image.shape[1]  # width
        self.height = image.shape[0]  # height

        # ground
        self.ground_level = int(self.height * 0.15 * 10 / 10)
        self.ground_color = (75, 180, 70)
        self.ground_line_thickness = -1

        # sky
        self.skyColor = (255, 255, 85)  # BGR, not RGB
        self.sky_line_thickness = -1

    def _draw_sky(self):
        x1, y1 = 0, 0
        x2, y2 = self.width, self.height - self.ground_level
        print(f'ground level={self.ground_level}, y2={y2}')
        cv.rectangle(self.bg, (x1, y1), (x2, y2), self.skyColor, self.sky_line_thickness)

    def _draw_ground(self):
        x1, y1 = 0, self.height - self.ground_level
        x2, y2 = self.width, self.height
        cv.rectangle(self.bg, (x1, y1), (x2, y2), self.ground_color, self.ground_line_thickness)

    def draw_background(self):
        self._draw_sky()
        self._draw_ground()