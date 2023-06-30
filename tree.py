import cv2 as cv
import numpy as np

class Tree:
    def __init__(self, image, location):
        self.img = image
        self.loc = location # horizontal X position
        self.ht: int = self.img.shape[0]
        print(f'Tree ht={self.ht}')

    def draw(self):
        x1 = x2 = self.loc
        cv.line(self.img, (x1,y1), (x2, y2))
