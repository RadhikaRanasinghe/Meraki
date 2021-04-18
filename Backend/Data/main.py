import writing
import cv2

from extractPen import extractPen
from extractTemplate import extractTemplate

img = cv2.imread("handpd_images/HealthyMeander/mea1-H1.jpg")

img_pen = extractPen(img)
img_template = extractTemplate(img)

cv2.imshow('pen', img_pen)
cv2.waitKey(0)
cv2.imshow('template', img_template)
cv2.waitKey(0)


# writing.create_oversampling("detectpd_csv/DetectPD.csv")
