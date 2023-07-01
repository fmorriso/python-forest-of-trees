import cv2 as cv
from numpy import ndarray

#
color_brown = (30, 65, 155)


class Tree:
    def __init__(self, image: ndarray, horizontal_pct: float):
        # self.forest = forest
        self.img = image

        self.forest_height = self.img.shape[0]
        self.forest_width = self.img.shape[1]

        self.horizontal_pct: float = horizontal_pct  # % distance from left edge
        self.loc = int(self.forest_width * self.horizontal_pct)
        self.ht: int = int(self.forest_height * 0.30)  # 30% of available image height
        print(f'Tree ht={self.ht}')
        self.trunk_thickness = int(self.forest_width * 0.03)

    def draw(self) -> ndarray:
        # trunk
        x1 = x2 = self.loc
        y1 = self.forest_height - self.forest_ground_level  # bottom of line/trunk
        y2 = y1 - self.ht
        cv.line(self.img, (x1, y1), (x2, y2), self.color_brown, self.trunk_thickness)

        # leaves
        # TODO: *** code needed here ***
        return self.img
