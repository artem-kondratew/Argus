import cv2


class Image:
    def __init__(self, number):
        self.number = number
        zero = "0" if self.number < 10 else ""
        self.name = "img_{0}{1}".format(zero, str(self.number))
        path = "input/{}.jpeg".format(self.name)
        self.img = cv2.imread(path)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def save(self):
        filename = self.name + ".png"
        cv2.imwrite(filename, self.gray)
