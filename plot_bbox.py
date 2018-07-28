#-*- coding: utf-8 -*- 
import cv2


imgpath = "/Users/bin/Documents/比赛/卡口图片打标/train_1w/e3d5c101-6bb9-48af-ac80-08c73304456b.jpg"

x1 = 173
y1 = 179
w1 = 162
h1 = 180

x2 = 508
y2 = 197
w2 = 157
h2 = 194

x_min = x1
y_min = y1
x_max = x1 + w1 - 1 
y_max = y1 + h1 - 1 

x_min2 = x2
y_min2 = y2
x_max2 = x2 + w2 - 1
y_max2 = y2 + h2 - 1

img = cv2.imread(imgpath)
#173_179_162_180;508_197_157_194

cv2.rectangle(img, (int(x_min),int(y_min)), (int(x_max), int(y_max)),(0,255,0),3)
cv2.rectangle(img, (int(x_min2),int(y_min2)), (int(x_max2), int(y_max2)),(0,255,0),3)
if (y_min > 10):
    cv2.putText(img, "car1", (int(x_min),int(y_min-6)), cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8, (0, 255, 0) )
else:

    cv2.putText(img, "car1", (int(x_min),int(y_min+15)), cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8, (0, 255, 0) )
#图片， 左上角， 右下角， 颜色， 线条粗细， 线条类型，点类型

if (y_min > 10):
    cv2.putText(img, "car2", (int(x_min2),int(y_min2-6)), cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8, (0, 255, 0) )
else:

    cv2.putText(img, "car2", (int(x_min2),int(y_min2+15)), cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8, (0, 255, 0) )
#图片， 左上角， 右下角， 颜色， 线条粗细， 线条类型，点类型
print img
cv2.imshow("img", img)
cv2.waitKey(0)
