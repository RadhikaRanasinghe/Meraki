import cv2

BLUR_RADIUS = 5


def extractPen(img):
    img = cv2.blur(img, (BLUR_RADIUS, BLUR_RADIUS))
    img = cv2.medianBlur(img, 11)

    if not img.data:
        print("No image data \n")
        return -1

    for i in img:
        for color in i:
            if (color[0] > 200 and color[1] > 200 and color[2] > 200) or color[0] < 70:
                color[0] = 255
                color[1] = 255
                color[2] = 255

    erosion_type = cv2.MORPH_RECT
    erosion_size = 1
    element = cv2.getStructuringElement(erosion_type, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                        (erosion_size, erosion_size))

    img = cv2.dilate(img, element)
    img = cv2.dilate(img, element)

    erosion_size = 2
    element1 = cv2.getStructuringElement(erosion_type, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                         (erosion_size, erosion_size))
    img = cv2.erode(img, element1)

    for i in img:
        for color in i:
            difRG = abs(int(color[0]) - int(color[1]))
            difRB = abs(int(color[0]) - int(color[2]))
            difGB = abs(int(color[1]) - int(color[2]))
            if difGB < 30 and difRB < 30 and difRG < 40:
                color[0] = 255
                color[1] = 255
                color[2] = 255

    img = cv2.blur(img, (BLUR_RADIUS, BLUR_RADIUS))
    img = cv2.medianBlur(img, 3)

    return img
