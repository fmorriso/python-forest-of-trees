import cv2 as cv
from numpy import ndarray
# project classes:
from forest import Forest


class Tree:
    def __init__(self, forest:Forest, image: ndarray, horizontal_pct: float):
        self.forest = forest
        self.img = image
        self.horizontal_pct: float = horizontal_pct # % distance from left edge
        self.loc = int(forest.width * self.horizontal_pct)
        self.ht: int = int(forest.height * 0.30) # 30% of available image height
        print(f'Tree ht={self.ht}')
        self.trunk_thickness = int(self.forest.width * 0.03)

    def draw(self) -> ndarray:
        # trunk
        x1 = x2 = self.loc
        y1 = self.forest.height - self.forest.ground_level # bottom of line/trunk
        y2 = y1 - self.ht
        cv.line(self.img, (x1,y1), (x2, y2), self.forest.brown, self.trunk_thickness)
        return self.img
