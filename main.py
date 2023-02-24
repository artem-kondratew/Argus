import numpy as np
import cv2
import os
from Object import Object
from Image import Image


inp = Image(2)
obj = Object((32, 88, 135), (44, 255, 230), 10)
obj.save()
inp.save()

res = cv2.matchTemplate(inp.gray, obj.gray, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(min_val, max_val, min_loc, max_loc)

a = [[[[]]]]
a = cv2.rectangle(inp.img, max_loc, (max_loc[0] + obj.height * 4, max_loc[1] + obj.width * 4), (0, 0, 255), 3)

if not a[0][0][0]:
    pass  # Проверка на наличие рисунка на изображении.
    print("HERE")
else:
    inp.img = cv2.resize(inp.img, (600, 800))
    cv2.imwrite("result.png", inp.img)
    cv2.waitKey(0)
