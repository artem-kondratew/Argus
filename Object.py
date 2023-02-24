import cv2
import numpy as np


class Object:

    def find_max_area(self):
        total, pixel_values, stats, centroids = cv2.connectedComponentsWithStats(self.bin)

        areas = stats[1:, -1]
        total -= 1
        min_area = 10000
        max_area_frame = np.zeros(self.bin.shape, dtype=np.uint8)

        for i in range(0, total):
            if areas[i] >= min_area:
                max_area_frame[pixel_values == i + 1] = int(255)
        return max_area_frame

    def __init__(self, min_hsv, max_hsv, number):
        self.number = number
        self.min_hsv = min_hsv
        self.max_hsv = max_hsv
        self.name = "obj{}".format(str(self.number))
        path = "objects/{}.png".format(self.name)
        self.img = cv2.imread(path)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        self.bin = cv2.inRange(self.hsv, self.min_hsv, self.max_hsv)
        self.max_area = Object.find_max_area(self)
        self.height = self.gray.shape[0]
        self.width = self.gray.shape[1]

    def save(self):
        filename = self.name + ".png"
        cv2.imwrite(filename, self.gray)
